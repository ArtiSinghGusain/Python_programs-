

numbers = [1,2,3,4,5,6,7,8,9]

total = 0

for num in numbers:
    total += num

print(total)

#Pythonic way

numbers = [1,2,3,4,5,6,7,8,9]
print(sum(numbers))

#List comprehension

total = sum([num for num in numbers])
print(total)