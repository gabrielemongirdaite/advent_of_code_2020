import pandas as pd
import numpy as np
import time
import re
import math
from sympy.ntheory.modular import crt

start_time = time.time()
df = pd.read_fwf('input_d13.txt', header=None)
l = df.loc[:, 0].tolist()
depart = int(l[0])
buses = re.findall(r'\b\d+\b', l[1])
l_1 = l[1].split(',')
timestamps = [l_1.index(i) for i in buses]
buses = [int(i) for i in buses]


possible_combo = []
smallest = float('inf')
bus = 0
for i in buses:
    closest_departure_div = depart//i
    closest_departure_mod = depart % i
    (smallest, bus) = (i-closest_departure_mod, i) if i-closest_departure_mod<smallest else (smallest, bus)

print('1st part answer: ' + str(smallest * bus))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


# Chinese remainder theorem e.g. http://homepages.math.uic.edu/~leon/mcs425-s08/handouts/chinese_remainder.pdf
rem = [x1 - x2 for (x1, x2) in zip(buses, timestamps)]
print("2nd part answer: ", crt(buses, rem)[0])