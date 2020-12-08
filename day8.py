import pandas as pd
import numpy as np
import time
import copy


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        lines_final = []
        for line in file_in:
            lines.append(line.rstrip("\n"))

        for i in lines:
            line_split = i.split(' ')
            lines_final.append([line_split[0], int(line_split[1])])

    return lines_final


def actions(operation, argument, accumulator_sum, current_position):
    if operation == 'acc':
        accumulator_sum += argument
        current_position += 1
    elif operation == 'jmp':
        current_position += argument
    else:
        current_position += 1
    return accumulator_sum, current_position


def accumulator(lst):
    visited = [False] * (len(lst))
    i = 0
    accumulator_sum = 0
    while not visited[i]:
        visited[i] = True
        accumulator_sum, i = actions(lst[i][0], lst[i][1], accumulator_sum, i)
    return accumulator_sum


def accumulator_part2(lst):
    for j in lst:
        if j[0] in ['nop', 'jmp']:
            visited = [False] * (len(lst))
            i = 0
            accumulator_sum = 0
            lst_copy = copy.deepcopy(lst)
            index_lst = lst_copy.index(j)
            lst_copy[index_lst][0] = 'nop' if j[0] == 'jmp' else 'nop'
            while not visited[i]:
                visited[i] = True
                accumulator_sum, i = actions(lst_copy[i][0], lst_copy[i][1], accumulator_sum, i)
                if i >= len(visited):
                    return accumulator_sum


start_time = time.time()
print('1st part answer: ' + str(accumulator(read_file('input_d8.txt'))))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: ' + str(accumulator_part2(read_file('input_d8.txt'))))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
