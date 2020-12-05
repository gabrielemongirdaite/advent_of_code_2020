import pandas as pd
import numpy as np
import time


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            lines.append(line.rstrip("\n"))
    return lines


def divide_and_choose(range_size, direction, lower, higher):
    new_size = len(range_size) // 2
    if direction == lower:
        lower_interval = range_size[0]
        upper_interval = range_size[new_size]
    elif new_size == 0:
        lower_interval = range_size.stop
        upper_interval = range_size.stop
    else:
        lower_interval = range_size[new_size + 1]
        upper_interval = range_size[len(range_size) - 1] + 1
    return range(lower_interval, upper_interval)


def find_row(entry):
    entry_rel = entry[0:7]
    range_size = range(127)
    for i in entry_rel:
        range_size = divide_and_choose(range_size, i, 'F', 'B')
    return range_size.start


def find_seat(entry):
    entry_rel = entry[7:]
    range_size = range(7)
    for i in entry_rel:
        range_size = divide_and_choose(range_size, i, 'L', 'R')
    return range_size.start


start_time = time.time()
lines = read_file("input_d5.txt")
ids = []
for i in lines:
    ids.append(find_row(i) * 8 + find_seat(i))

print('1st part answer: ' + str(max(ids)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
all_ids = []
for i in range(127):
    for j in range(7):
        all_ids.append(i * 8 + j)

not_in_list = np.setdiff1d(all_ids, ids)

# This part is not nicely written. I.e. it is observed from not_in_list which is the right seat.

correct = []
i = 0
while i < len(not_in_list):
    try:
        if not_in_list[i] + 1 != not_in_list[i + 1] and not_in_list[i] + 2 != not_in_list[i + 1]:
            correct.append(not_in_list[i + 1])
    except:
        print('end')
    i += 2

print('2nd part answer: ' + str(correct[0]))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
