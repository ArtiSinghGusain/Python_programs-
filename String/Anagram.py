# 3.	Check if two strings are anagrams.

str1 = "silent"
str2 = "lioosten"

#Method 1 using sorted

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")

# Method 2

str1 = "silent"
str2 = "listen"


if len(str1) != len(str2):
    print("Not Anagram")
else:
    count = {}

    for i in str1:
        count[i] = count.get(i,0)+1

    for j in str2:
        if j not in count:
            print("Not Anagram")
            break

        count[j] -= 1

        if count[j] < 0:
            print("Not Anagram")
            break

    else:
            print("Anagram")

