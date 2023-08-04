import pandas as pd
import numpy as np

#data = pd.Series("/home/leong/Documents/data.csv")
#data.head()
#data.value_counts()

#df = pd.read_csv (r'/home/leong/Documents/data.csv')
#print (df)

#data = pd.read_csv('/home/leong/Documents/data.csv')
#freq_dis_col1 = data.csv['col1'].value_counts()
#freq_dis_col1

import pandas
import math
import matplotlib.pyplot as plt
import numpy as np

data = [28, 22, 23, 20, 12, 24, 37, 28, 21, 25,
        21, 14, 30, 23, 27, 13, 23, 7, 26, 19,
        24, 22, 26, 3, 21, 24, 28, 40, 27, 24,
        20, 25, 23, 26, 47, 21, 29, 26, 22, 33,
        27, 9, 13, 35, 20, 16, 20, 25, 18, 22]

classes = 8
range_of_data = max(data) - min(data)
size_of_class = range_of_data / classes
print(f"range is {range_of_data} and size is {size_of_class}")
# print(max(data), min(data))
Class = [3]
count = 3
while True:
    count += size_of_class
    Class.append(count)
    if count == max(data):
        break

Class_mid_point = []
for item in Class[1:]:
    avg = item / 2
    Class_mid_point.append(round(avg, 2))

frequency = []
number = 0
for item in Class:
    if item != Class[len(Class) - 1]:
        for items in range(math.floor(item), round(size_of_class + item)):
            for items_ in data:
                if items == items_:
                    number += 1
        frequency.append(number)
        number = 0

cumulative_frequency = [3]
sums = 0
for i in Class[1:]:
    for j in range(0, Class.index(i) + 1):
        sums = Class[0] + Class[j]
    cumulative_frequency.append(sums)
    sums = 0

upper_class_boundary = []
for items in Class:
    upper_class_boundary.append(items + 0.05)

values, base = np.histogram(cumulative_frequency, upper_class_boundary)

cum_sum = np.cumsum(values)

plt.plot(base[1:], cum_sum, color='red', marker='o', linestyle='-')

plt.title('Ogive Graph')
plt.xlabel('upper class frequency')
plt.ylabel('Cumulative Frequency')
plt.show()



