# 19.	Find common elements between two lists


list1 = [1,22,3,4,5]
list2 = [44,55,22,22,22,33,55]

set2 = set(list2)
common_element = []

for i in list1:
    if i in set2:
        common_element.append(i)

print(common_element)

#Using set intersection

list1 = [1,22,3,4,5]
list2 = [44,55,22,22,22,33,55]

common = list(set(list1) & set(list2))

print(common)