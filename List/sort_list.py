# 17.	Sort list without using sort()
#Selection Sort
list1 = [69,1,3,4,622,4,6,66,7,68]

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print(list1)