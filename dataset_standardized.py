import csv
import random 

# reads dataset from csv file 
def read_healthcare(): 
    with open("healthcare-dataset-stroke-data.csv", "r") as file:
        return list(csv.DictReader(file))

# standardizes dataset
def standardize(set, attr):
    # filters nonnumeric values out of set
    num = [float(row[attr]) for row in set if row[attr].strip() and row[attr].replace('.', '', 1).isdigit()]
    
    # Calculate average
    avg = sum(num) / len(num)
    
    # calculate standardization
    final = (sum((x - avg) ** 2 for x in num) / len(num)) ** 0.5

    # apply standardization and formatting
    for row in set: 
        if row[attr].strip() and row[attr].replace('.', '', 1).isdigit():
            val = (float(row[attr]) - avg) / final
            row[attr] = f"{val:.2f}"
    return set

# read dataset
set = read_healthcare()

# Standardize age
set = standardize(set, 'age')

# Standardize bmi
set = standardize(set, 'bmi')

# copies data to new file with new standardization values
def copy_file(source, dest):
    with open(dest, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        
        # Write each row with the standardized 'age' and 'bmi' values to the new CSV file
        for row in source: 
            writer.writerow([row['id'], row['age'], row['bmi']])

# output file 
output = "standardized.csv"

# copies data to new csv file
copy_file(set, output)

print(f"{output} saved")

