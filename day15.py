import time

lst = [0, 6, 1, 7, 2, 19, 20]

i = len(lst)
answer = []
answer.extend(lst)
while i < 2020:
    if answer[i-1] not in answer[0:i-1]:
        answer.append(0)
    else:
        age = len(answer[0:i-1]) - answer[0:i-1][::-1].index(answer[i-1])
        answer.append(i - age)
    i += 1

start_time = time.time()
print('1st part answer: ', answer[2019])
print("--- %s seconds for 1st part---" % (time.time() - start_time))

