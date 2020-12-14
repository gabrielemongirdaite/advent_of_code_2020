import pandas as pd
import numpy as np
import time
import re
import itertools


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            lines.append(line.replace('\n', ''))
    return lines


def create_memory(lst):
    memory = {}
    for i in lst:
        if i[0:4] == 'mask':
            mask = i.split()[2]
        else:
            index = re.findall(r'\b\d+\b', i)[0]
            value = re.findall(r'\b\d+\b', i)[1]
            result = list('{0:036b}'.format(int(value)))
            k = 0
            for j in list(mask):
                if j != 'X':
                    result[k] = j
                k += 1
            memory[index] = int(''.join(str(n) for n in result),2)
    return memory

def permutations_with_replacement(n, choices):
    l = [choices] * n
    return list(itertools.product(*l))


def create_memory_part2(lst):
    memory = {}
    for i in lst:
        if i[0:4] == 'mask':
            mask = i.split()[2]
        else:
            index = re.findall(r'\b\d+\b', i)[0]
            value = re.findall(r'\b\d+\b', i)[1]
            result = list('{0:036b}'.format(int(index)))
            k = 0
            for j in list(mask):
                if j in ('X', '1'):
                    result[k] = j
                k += 1
            indices = [i for i, x in enumerate(result) if x == "X"]
            for per in permutations_with_replacement(len(indices), [0, 1]):
                for l, m in zip(range(len(per)), indices): result[m] = per[l]
                memory[int(''.join(str(n) for n in result), 2)] = int(value)
    return memory


def memorySum(memory):
    memory_sum = 0
    for i in memory:
        memory_sum += memory[i]
    return memory_sum

l = read_file('input_d14.txt')
start_time = time.time()
print('1st part answer: ', memorySum(create_memory(l)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: ', memorySum(create_memory_part2(l)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))