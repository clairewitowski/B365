import csv
import pandas as pd
import math
import numpy as np

x = [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0,
        1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1,
        1, 0, 1, 0, 1, 1]
y= [0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1,
        0, 1, 0, 0, 0, 0]

# finds exactly where the values in each array equals 1 
a = {i for i in range(len(x)) if x[i] == 1}
b = {i for i in range(len(y)) if y[i] == 1}
# gives the intersection per the jaccard similarity formula 
inter = len(a & b)
# gives the union per the jaccard similarity formula 
u = len(a | b)
# divides the jaccard similarity using the intersection and union
jaccard_similarity = inter / u
# rounds the similarity to two decimal places
jaccard_similarity = round(jaccard_similarity, 2)

# print the result
print(jaccard_similarity)
print('0.01')
