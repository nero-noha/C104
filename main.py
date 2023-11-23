from collections import Counter
import pandas as pd
import plotly.express as px

import csv

df = pd.read_csv("data.csv")

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data=[]

for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

n = len(new_data)
total = 0

for x in new_data : 
    total += x

mean = total / n
print("Mean / Average is: " + str(mean))

if n % 2 == 0:
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2 - 1])
    median = (median1 + median2)/2
else:
    median = new_data[n//2]
    print(n)
print("Median is: " +str(median))

data = Counter(new_data)
mode_data_for_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
    }

for height, occurrence in data.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurrence 
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurrence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurrence

mode_range, mode_occurrence = 0, 0

for range, occurrence in mode_data_for_range.items() :
    if occurrence > mode_occurrence:
        range_values = range.split(" - ")
        mode_range = [int(range_values[0]), int(range_values[1])]
        mode_occurrence = occurrence

mode = float((mode_range[0] + mode_range[1]) / 2)
print("Mode is -> {mode:2f}")