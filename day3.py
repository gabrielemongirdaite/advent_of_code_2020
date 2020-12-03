import pandas as pd
import numpy as np
import time


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            line_int = line.replace('.', '0').rstrip("\n")
            line_int = line_int.replace('#', '1')
            res = []
            res[:] = line_int
            res = list(map(int, res))
            lines.append(res)
    return lines


def repeat(x, cycle):
    new_x = x % cycle
    return new_x


def coordinates(lines, right, down):
    width_= len(lines[0])
    length_ = len(lines)
    coor = []
    x = 0
    for i in range(length_):
        x += right
        coor.append((repeat(x, width_), (i+1)*down))
    return coor


def count_trees(coor, lines):
    cnt = 0
    for i in coor:
        try:
            cnt = cnt + lines[i[1]][i[0]]
        except:
            cnt = cnt
    return cnt


lines = read_file("input_d3.txt")
coor_31 = coordinates(lines, 3, 1)
cnt_31 = count_trees(coor_31, lines)
coor_11 = coordinates(lines, 1, 1)
cnt_11 = count_trees(coor_11, lines)
coor_51 = coordinates(lines, 5, 1)
cnt_51 = count_trees(coor_51, lines)
coor_71 = coordinates(lines, 7, 1)
cnt_71 = count_trees(coor_71, lines)
coor_12 = coordinates(lines, 1, 2)
cnt_12 = count_trees(coor_12, lines)
answer = cnt_11*cnt_12*cnt_51*cnt_71*cnt_31

print('1st part answer: ' + str(cnt_31))
print('2nd part answer: ' + str(answer))