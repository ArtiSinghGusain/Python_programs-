#find min and max element in a list without min/max function

list1 = [12,122,3,20]
#Method 1 Traverse the List

min = list1[0]
max = list1[0]

for i in list1:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)

#2nd Approach Sort the List

list1 = [12,122,3,20]

for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]

print(list1[0],list1[-1])