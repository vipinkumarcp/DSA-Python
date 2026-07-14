# defaultdict

# defaultdict is a dictionary that automatically creates a default value for a missing key.

from collections import defaultdict

student = defaultdict(list)

student["math"].append(90)

print(student)

count = defaultdict(int)

text = "banana"

for i in text:
    count[i] +=1

print(count)

# Grouping Values

data = [
    ("A",50),
    ("B",30),
    ("A",67)
]

groups = defaultdict(list)
for key,value in data:

    groups[key].append(value)

print(groups)