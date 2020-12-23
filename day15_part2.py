import time
import numpy as np

start_time = time.time()
lst = [np.inf, 0, 6, 1, 7, 2, 19, 20]

i = len(lst)
answer = []
answer.extend(lst)
numbers_dict = {k: v for v, k in enumerate(answer)}

while i <= 30000000:
    if answer[i-1] not in numbers_dict:
        answer.append(0)
        numbers_dict[answer[i-1]] = i-1
    else:
        age = i - 1 - numbers_dict[answer[i-1]]
        answer.append(age)
        numbers_dict[answer[i - 1]] = i-1
    i += 1


print('2nd part answer: ', answer[30000000])
print("--- %s seconds for 2nd part---" % (time.time() - start_time))

