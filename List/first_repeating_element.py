#find first repeating element in a list


list1 = [21,34,6,78,9,7,6,66]

first_repeating_element = ""
count = {}

for i in list1:
    count[i] = count.get(i,0)+1

    if count[i] == 2:
        print(i)
        break


#Second Approach

list1 = [21,34,6,78,9,7,6,66]

seen = set()

for i in list1:
    if i in seen:
        print(i)
        break
    seen.add(i)




