
list1 = [69,1,3,4,622,4,6,66,7,68]

highest_num = 0
second_highest_num = 0

for i in list1:
    if i >highest_num:
        second_highest_num = highest_num
        highest_num = i
    elif highest_num > i > second_highest_num:
        second_highest_num = i

print(second_highest_num)