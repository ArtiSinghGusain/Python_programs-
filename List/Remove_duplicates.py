# Remove duplicates from the list

list1 = ["Python", "is", "Programming", "Lang", "Love", "Python"]

unique = []

for i in list1:
    if i not in unique:
        unique.append(i)

print(unique)