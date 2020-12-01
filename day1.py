import pandas as pd
import numpy as np
import time


def read_file(file_name):
    with open(file_name) as file_in:
        lines = []
        for line in file_in:
            lines.append(int(line))
    return lines

def sum_2020_2(list_data):
    answer = 0
    n=0
    for i in list_data:
        for j in list_data[list_data.index(i)+1:len(list_data)]:
            n+=1
            if i+j == 2020:
                answer = i*j
                break
    return answer

def sum_2020_3(list_data):
    answer = 0
    n=0
    for i in list_data:
        for j in list_data[list_data.index(i)+1:len(list_data)]:
            for k in list_data[list_data.index(j)+1:len(list_data)]:
                n+=1
                if i+j+k == 2020:
                    answer = i*j*k
                    break
    return answer

start_time = time.time()
print('1st part answer: '+ str(sum_2020_2(read_file("input_d1.txt"))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: '+ str(sum_2020_3(read_file("input_d1.txt"))))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
