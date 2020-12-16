import re
import pandas as pd
import copy
import time


def read_file(file):
    my_file = open(file, "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    content_list =[sub.replace('\n', ' ') for sub in content_list]
    possible_numbers = {}
    all_numbers = []
    for i in content_list:
        splitted = i.split(': ')
        numbers = re.findall(r'\b\d+\b', splitted[1])
        lst_num = list(range(int(numbers[0]), int(numbers[1])+1)) + list(range(int(numbers[2]), int(numbers[3])+1))
        all_numbers.extend(lst_num)
        possible_numbers[splitted[0]] = lst_num
    return possible_numbers, all_numbers

lst, numbers = read_file('input_d16_numbers.txt')

df = pd.read_fwf('input_d16_tickets.txt', header=None)
l = df.loc[:, 0].tolist()
tickets = []
for i in l:
    tickets.append(list(map(int, i.split(','))))

bad_numbers = []
tickets_full = copy.deepcopy(tickets)
for tic in tickets_full:
    for num in tic:
        if num not in numbers:
            bad_numbers.append(num)
            tickets.remove(tic)

start_time = time.time()
print('1st part answer: ', sum(bad_numbers))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


categories = [list(x) for x in zip(*tickets)]

def assign_categories(category, features, cat):
    choices = {}
    k = 0
    for i in category:
        choices[cat[k]] = []
        for j in features:
            if set(i).issubset(set(features[j])):
                choices[cat[k]].append(j)
        k += 1
    return choices


def map_correctly(category, features):
    cat = list(range(0,20))
    choices = assign_categories(category, features, cat)
    result = []
    while len(choices)>=1:
        min_len = min(map(len, choices.values()))
        res = {k: v for k, v in choices.items() if len(v) == min_len}
        result.append(res)
        being_removed = list(res.keys())[0]
        features.pop(res[being_removed][0])
        cat.remove(being_removed)
        new_category = [category[m] for m in cat]
        choices = assign_categories(new_category, features, cat)
    return result

start_time = time.time()
print(map_correctly(categories, lst))
print('2nd part answer: ', tickets_full[0][16]*tickets_full[0][1]*tickets_full[0][14]*tickets_full[0][17]*tickets_full[0][2]*tickets_full[0][6])
print("--- %s seconds for 2nd part---" % (time.time() - start_time))