import csv
import pandas as pd
import math
import numpy as np

# reads the csv dataset file 
def read_customers(): 
    with open("bank_customers.csv", "r") as file:
        return list(csv.DictReader(file))

def distance(pointA, pointB):
    total = 0
    for i in range(len(pointA)):
        total = sum((float(a) - float(b)) ** 2 for a, b in zip(pointA, pointB))
    return math.sqrt(total)

def pairs(paths, cap=5):
    reader = pd.read_csv(paths)

    if 'CustomerId' in reader.columns:
        reader = reader.drop(columns=['CustomerId'])

    data_list = reader.astype(float).values.tolist()

    counter = 0
    nums = len(data_list)
    for i in range(nums):
        for j in range(i + 1, nums):
            euc = distance(data_list[i], data_list[j])
            if euc < cap:
                counter += 1 
                
    print(counter)

paths = 'bank_customers.csv'
pairs(paths)  

print('123')