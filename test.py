# C:\Users\newwo\OneDrive\바탕 화면\20240211_파이썬테스트\test.py

# 1. python -> pip
# 2. node -> npm npx

import csv
import matplotlib.pyplot as plt
import pandas as pd

x = []
y = []
f = open('data.csv', 'r', encoding='UTF8')
reader = csv.reader(f)

for row in reader:
    x.append(str(row[1]))
    if (int(row[7]) > 70) : print(row[7])
    y.append(int(row[7]))
f.close()

defaultDpi = 100
plt.figure(figsize=(1200/defaultDpi, 300/defaultDpi), dpi=defaultDpi)
plt.scatter(x, y, c=[(0, 0, 0)], marker='s', s=2)
plt.title('TEST')
plt.xlabel('year')
plt.ylabel('people')
plt.show()









# python

# string (문자열) -> 원명주

# print("원명주")

# value = "4 5"
# print(value.strip().split(' '))
# [4, 5]