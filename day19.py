import time
import re
import itertools
import pandas as pd
from collections import Counter
import numpy as np


def isListEmpty(inList):
    if isinstance(inList, list): # Is a list
        return all( map(isListEmpty, inList) )
    return False # Not a list


def fix_list(key, dct, new_lst):
    for i in dct[key]:
        new = i.replace(" ", "").replace('"', '')
        new_lst.append(new)
    return new_lst


def read_file(file):
    my_file = open(file, "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    content_list =[sub.split(': ') for sub in content_list]
    content_dict = {item[0]: ' '+item[1]+' ' for item in content_list}
    return content_dict


def split_value(dct):
    for i in dct:
        try:
            value = dct[i].split('|')
        except:
            value = dct[i]
        dct[i] = value
    return dct


def find_only_letters(dct):
    letters = []
    for i in dct:
        if isListEmpty([re.findall(r'\b\d+\b', dct[i][j[0]]) for j in enumerate(dct[i])]):
            letters.append((i, dct[i]))
    return letters


def adjust_dict(dct, letters):
    for i in dct:
        for j in letters:
            try:
                if any([j[0] in dct[i][k] for k in range(len(dct[i]))]):
                    dct[i] = dct[i] * len(j[1])
                    dct[i] = [re.sub(' '+j[0]+' ', ' '+j[1][l]+' ', dct[i][k]) for k, l in list(itertools.product(range(len(dct[i])), range(len(j[1]))))]
                    dct[i].sort()
                    dct[i] = list(dct[i] for dct[i], _ in itertools.groupby(dct[i]))
            except:
                pass
    return dct


def check_rules(str):
    numbers = [int(s) for s in re.findall(r'\b\d+\b', str)]
    num_dct = dict(Counter(numbers))
    try:
        dup42 = num_dct[42]
        last41 = len(numbers) - 1 - numbers[::-1].index(42)
    except:
        dup42 = 0
        last41 = np.inf
    try:
        dup31 = num_dct[31]
        first31 = numbers.index(31)
    except:
        dup31 = 0
        first31 = 0
    if dup42 >= dup31 + 1 and last41 < first31:
        return True
    else:
        return False


start_time = time.time()
dct = read_file('input_d19_instructions.txt')
dct = split_value(dct)
while not isListEmpty([re.findall(r'\b\d+\b', dct['11'][j[0]]) for j in enumerate(dct['11'])]) \
        or not isListEmpty([re.findall(r'\b\d+\b', dct['8'][j[0]]) for j in enumerate(dct['8'])]):
    letters = find_only_letters(dct)
    dct = adjust_dict(dct, letters)

all8 = []
all8 = fix_list('8', dct, all8)

all11 = []
all11 = fix_list('11', dct, all11)

df = pd.read_fwf('input_d19_messages.txt', header=None)
l = df.loc[:, 0].tolist()
cnt = 0
for i in l:
    if i[0:len(all8[0])] in all8 and i[len(all8[0]):] in all11:
        cnt += 1

print('1st part answer: ', cnt)
print("--- %s seconds for 1st part---" % (time.time() - start_time))

# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
answer = 0
all42 = []
all42 = fix_list('42', dct, all42)

all31 = []
all31 = fix_list('31', dct, all31)


for i in l:
    composition = ''
    chunks, chunk_size = len(i), 8
    for j in [ i[k:k+chunk_size] for k in range(0, chunks, chunk_size) ]:
        if j in all42:
            composition += '42 '
        elif j in all31:
            composition += '31 '
        else:
            composition += 'NA '
    answer += check_rules(composition)

print('2nd part answer: ', answer)
print("--- %s seconds for 2nd part---" % (time.time() - start_time))