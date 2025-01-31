import csv
import random

# 2.2: Random Sampling 
# reads dataset and performs random sampling with replacement 
# returns required dataset information but with a sample size of 35%

# reads the csv dataset file 
def read_healthcare(): 
    with open("healthcare-dataset-stroke-data.csv", "r") as file:
        return list(csv.DictReader(file))

# declares the opened dataset as a variable 
dataset = read_healthcare()

# chooses random patients from the dataset 
def pick_random(set, p):  
    return [random.choice(dataset) for _ in range(size)]

# shortens the dataset down to 35% 
size = int(len(dataset) * 0.35)

# utilizes random function with dataset and required size 
sorted_data = pick_random(dataset, size)

# cleans all of the data in the same way as problem
def clean35(dataset):

    females = 0
    hypertension = 0
    never_smoked = 0 
    age = 0
    patients = 0

    for row in dataset: 
        patients = patients + 1     # computes total number of patients

        if row['age']:
            age = age + float(row['age'])   # adds all patient ages

        if row['gender'] == 'Female':
            females += 1    # keeps count of female patients

        if row['hypertension'] == '1':
            hypertension = hypertension + 1  # keeps count of hypertension patients

        if row['smoking_status'] == 'never smoked':
            never_smoked = never_smoked + 1    # keeps count of patients who don't smoke

    mean = age / patients

    percent = (hypertension / patients) * 100

    # returns the required criteria to 2 decimal places for floats
    return f"{females}, {mean:.2f}, {percent:.2f}, {never_smoked}"

# prints the shortened and randomized dataset
print(clean35(sorted_data))
