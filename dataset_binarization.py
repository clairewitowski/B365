import csv
import random

# 2.3: Binarization
# generates copy of dataset with only id and smoking status 
# returns numerical values only, and smoking status as one hot val

# reads dataset
def read_healthcare(): 
    with open("healthcare-dataset-stroke-data.csv", "r") as file:
        return list(csv.DictReader(file))

# turns smoking status attributes into one-hot numerical vals
def smoking(dataset):
    for row in dataset:
        if row['smoking_status'] == 'Unknown':
            row['Unknown'] = 1 
        else:
            row['Unknown'] = 0
            
        if row['smoking_status'] == 'never smoked':
            row['never smoked'] = 1 
        else:
            row['never smoked'] = 0

        if row['smoking_status'] == 'smokes':
            row['smokes'] = 1 
        else:
            row['smokes'] = 0

        if row['smoking_status'] == 'formerly smoked':
            row['formerly smoked'] = 1 
        else:
            row['formerly smoked'] = 0
    return dataset

# reads the dataset csv file
dataset = read_healthcare()

# apply one-hot to dataset
one_hot = smoking(dataset)

# copy dataset to new csv file
def copy_file(source, dest):
    with open(dest, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        for row in source: 
            writer.writerow([row['id'], row['Unknown'], row['never smoked'], row['smokes'], row['formerly smoked']])

# create new csv file
output = "binarized.csv"
copy_file(one_hot, output)

print(f"{output} saved")

