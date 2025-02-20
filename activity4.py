import random

observations = []

for i in range(10):
    observation = random.randint(1,6)
    observations.append(observation)

print("observations:\n", observations)

sort = sorted(observations)

length = len(sort)
med = (sort[length // 2] + sort[(length-1) // 2]) / 2
print("median:\n", med)