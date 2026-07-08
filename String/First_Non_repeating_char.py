# 5.	Find first non-repeating character in a string. Done

string1 = "PythonProgramming"

freq = {}

for i in string1:
    freq[i] = freq.get(i,0)+1

for k,v in freq.items():
    if v == 1:
        print(k)
        break
