import pandas as pd
import numpy as np
import time


def read_file(file):
    my_file = open(file, "r")
    content = my_file.read()
    content_list = content.split("\n\n")
    my_file.close()
    content_list =[sub.replace('\n', '') for sub in content_list]
    return content_list


def anyone_answered(lines):
    cnt = 0
    for i in lines:
        cnt += len(''.join(set(i)))
    return cnt

start_time = time.time()
lines = read_file('input_d6.txt')
print('1st part answer: ' + str(anyone_answered(lines)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


def read_file_2(file):
    my_file = open(file, "r")
    content = my_file.read()
    content_list = content.split("\n\n")
    my_file.close()
    content_list =[sub.split('\n') for sub in content_list]
    return content_list


def everyone_answered(lines2):
    cnt = 0
    for i in lines2:
        to_list = ''.join(i)
        letters = ''.join(set(to_list))
        people = len(i)
        for j in letters:
            cnt_letter = 0
            for k in i:
                if j in k:
                    cnt_letter += 1
            if cnt_letter == people:
                cnt += 1
    return cnt


start_time = time.time()
lines2 = read_file_2('input_d6.txt')
print('2nd part answer: ' + str(everyone_answered(lines2)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))