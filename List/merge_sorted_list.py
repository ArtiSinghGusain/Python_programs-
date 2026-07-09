#merge two sorted list

list1 = [1,3,9]
list2 = [34,54,644]

list3 = sorted(list1 + list2)
print(list3)

for i in list2:
    list1.append(i)
print(sorted(list1))

# Best Approach two pointer Approach

list1 = [1,3,9]
list2 = [0,54,644]

i = 0
j = 0
result = []

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

while i < len(list1):
    result.append(list1[i])
    i += 1

while j < len(list2):
    result.append(list2[j])
    j += 1

print(result)


