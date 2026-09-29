#rotate a list by k element

numbers = [1, 2, 3, 4, 5]
k = 26
k %= len(numbers)
# k = 12 % 5  = 2
# right_rotation = [4,5,1,2,3]
# left_rotation = [3,4,5,1,2]

left_rotation = numbers[k:] + numbers[:k]
right_rotation = numbers[-k:] + numbers[:-k]

print(left_rotation)
print(right_rotation)