#Find Duplicates

list1 = ["Python", "is", "Programming", "Lang", "Love", "Python"]

unique = []
duplicates = []

for i in list1:
    if i not in unique:
        unique.append(i)
    else:
        duplicates.append(i)

print(duplicates)