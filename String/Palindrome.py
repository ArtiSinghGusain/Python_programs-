# 2.	Check if string is palindrome. - Done

name = "madam"

first_index = 0
last_index = len(name)-1

while first_index < last_index:
        if name[first_index] != name[last_index]:
            print("Not Palindrome")
            break

        first_index += 1
        last_index -= 1

else:
    print("Palindrome")
