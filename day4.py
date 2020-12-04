import pandas as pd
import numpy as np
import time
import re
import passport_fields

def read_file(file):
    my_file = open(file, "r")
    content = my_file.read()
    content_list = content.split("\n\n")
    my_file.close()
    content_list =[sub.replace('\n', ' ') for sub in content_list]
    return content_list


def extract_fields(content_list):
    fields = []
    for i in content_list:
        fields.append(re.split(':| ',i))
    return fields


def check_passport(fields):
    cnt = 0
    items = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
    for i in fields:
        cnt += items.issubset(set(i))
    return cnt

def create_dictionary(fields):
    list_dict = []
    for i in fields:
        dict = {}
        j = 0
        while j < len(i)-1:
            dict[i[j]] = i[j+1]
            j+=2
        list_dict.append(dict)
    return list_dict



start_time = time.time()
print('1st part answer: ' + str(check_passport(extract_fields(read_file("input_d4.txt")))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

entry_dict = create_dictionary(extract_fields(read_file("input_d4.txt")))
cnt = 0
for i in entry_dict:
    cnt_entry = 0
    passport_features = passport_fields.passport(i)
    if passport_features.check_items():
        cnt_entry += passport_features.check_birth_year()
        cnt_entry += passport_features.check_issue_year()
        cnt_entry += passport_features.check_expiry_year()
        cnt_entry += passport_features.check_height()
        cnt_entry += passport_features.check_hair()
        cnt_entry += passport_features.check_eyes()
        cnt_entry += passport_features.check_passport_id()
    if cnt_entry == 7:
        cnt += 1

print('2nd part answer: ' + str(cnt))

