# 2.	Check if string is palindrome. - Done

name = "madam"

first_index = 0 #0 , 1 , 2,
last_index = len(name)-1 #4, 3, 2

while first_index < last_index:
        if name[first_index] != name[last_index]:
            print("Not Palindrome")
            break

        first_index += 1
        last_index -= 1

else:
    print("Palindrome")
