import csv
import pandas as pd
import math
import numpy as np

def read_dataset(dataset):
    return pd.read_csv(dataset)

rds = read_dataset("B365_Titanic_Dataset.csv")
    
k = 20

rds['Age'] = (rds['Age'] - rds['Age'].mean()) / rds['Age'].std()
rds['Fare'] = (rds['Fare'] - rds['Fare'].mean()) / rds['Fare'].std()
rds['Sex'] = rds['Sex'].map({'female': 1, 'male': 0})

def dist(a, b):
    return math.sqrt(np.sum((a - b) ** 2))

def alg(rds, passenger, k):
    endDist = []
    for index, row in rds.iterrows():
        d = dist(row[['Sex', 'Age', 'Fare']].values, passenger)
        endDist.append(d)
    rds['Distance'] = endDist
    nn = rds.nsmallest(k, 'Distance')
    live = nn['Survived'].sum()
    die = k - live
    return live, die

person = np.array([1, 35, 50])
person = (person - rds[['Sex', 'Age', 'Fare']].mean()) / rds[['Sex', 'Age', 'Fare']].std()
live, die = alg(rds, person, k)
print(f'survived count:{live},casualty count:{die}')