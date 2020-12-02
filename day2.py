import pandas as pd
import numpy as np
import time
import collections


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    return lines


def subcomponents_lines(lines):
    lines2 = []
    for i in lines:
        min_ = int(i[:i.index("-")])
        max_ = int(i[i.index("-") + 1:i.index(" ")])
        character_ = i[i.index(" ") + 1:i.index(":")]
        password_ = i[i.index(":") + 2:].rstrip("\n")
        subset_ = [min_, max_, character_, password_]
        lines2.append(subset_)
    return lines2


def count_correct_passwords(lines2):
    cnt = 0
    for i in lines2:
        frequencies = collections.Counter(i[3])
        repetitions = frequencies[i[2]]
        if i[0] <= repetitions <= i[1]:
            cnt += 1
    return cnt


def count_correct_passwords_part_2(lines2):
    cnt = 0
    for i in lines2:
        if (i[3][i[0] - 1] == i[2] and i[3][i[1] - 1] != i[2]) or (i[3][i[0] - 1] != i[2] and i[3][i[1] - 1] == i[2]):
            cnt += 1
    return cnt


start_time = time.time()
print('1st part answer: ' + str(count_correct_passwords(subcomponents_lines(read_file("input_d2.txt")))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: ' + str(count_correct_passwords_part_2(subcomponents_lines(read_file("input_d2.txt")))))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
