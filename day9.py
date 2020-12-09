import pandas as pd
import numpy as np
import itertools
import time


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            lines.append(int(line))
    return lines


def find_all_sums(lst, r):
    all_sums = []
    for i in list(itertools.combinations(lst, r)):
        all_sums.append(sum(i))
    return all_sums


def crack_XMAS(lst):
    i = True
    preamble = lst[0:25]
    j = 25
    while i:
        if lst[j] in find_all_sums(preamble, 2):
            i = True
            preamble.append(lst[j])
            preamble.pop(0)
            j += 1
        else:
            i = False
    return lst[j]


def find_set(lst, invalid_number):
    for i in lst:
        sum_tmp = 0
        j = lst.index(i)
        while sum_tmp < invalid_number:
            sum_tmp += lst[j]
            if sum_tmp == invalid_number:
                return lst.index(i), j
            j += 1


start_time = time.time()
lst = read_file('input_d9.txt')
print('1st part answer: ' + str(crack_XMAS(lst)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
i, j = find_set(lst, 26796446)
lst_2 = lst[i:j+1]
print('2nd part answer: ' + str(min(lst_2)+max(lst_2)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))


