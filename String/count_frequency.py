# 4.	Count frequency of characters in a string.

string1 = "Python Programming"

freq = {}

for i in string1:
    freq[i] = freq.get(i,0)+1

print(freq)