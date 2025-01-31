import csv
# 2.1 : Dataset Analysis
# reads dataset and prints specific values on a single line with commas
# returns said line with the specified values 

# reads the csv dataset file 
def read_healthcare(): 
    with open("healthcare-dataset-stroke-data.csv", "r") as file:
        return list(csv.DictReader(file))

# declares the opened dataset as a variable 
dataset = read_healthcare()

# variable declaration
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
        females = females + 1    # keeps count of female patients

    if row['hypertension'] == '1':
        hypertension = hypertension + 1  # keeps count of hypertension patients

    if row['smoking_status'] == 'never smoked':
        never_smoked = never_smoked + 1    # keeps count of patients who don't smoke

# calculates average age of patients 
mean = age / patients

# gets hypertension percentage 
percent = (hypertension / patients) * 100

# prints out all of the required details with commas in between 
print(f"{females}, {mean:.2f}, {percent:.2f}, {never_smoked}")

    
