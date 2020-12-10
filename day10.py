import pandas as pd
import numpy as np
import time


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            lines.append(int(line))
        lines.sort()
    return lines


def jolt_differences(lst):
    jolt = 0
    dif_1 = 0
    dif_3 = 0
    for i in lst:
        if i - jolt == 1:
            dif_1 += 1
        elif i - jolt == 3:
            dif_3 += 1
        jolt = i
    return dif_1*(dif_3+1)


start_time = time.time()
print('1st part answer: ' + str(jolt_differences(read_file('input_d10.txt'))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


def create_dict(lst):
    dct = {}
    dct[0] = [i for i in lst if i <= 3]
    jolt = 0
    for i in lst:
        jolt = i
        dct[i] = [i for i in lst if 0 < (i - jolt) <= 3]
    return dct


start_time = time.time()
lst = read_file('input_d10.txt')
lst.append(0)
lst.sort()
dct = create_dict(lst)
paths_amount = [1] * len(dct)
for key in dct:
    i = 0
    repetitions = [0] * len(dct)
    if key == 0:
        repetitions[0] = 1
    while i < key:
        if key in dct[i]:
            repetitions[lst.index(i)] = 1
        i = lst[lst.index(i)+1]
    paths_amount[lst.index(key)] = sum([a*b for a, b in zip(repetitions, paths_amount)])


print('2nd part answer: ' + str(paths_amount[-1]))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))


