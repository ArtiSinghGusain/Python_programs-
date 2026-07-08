# 7.	Remove duplicate characters from string. Done

str1 = "PythonProgramming"

unique = ""

for i in str1:
    if i not in unique:
        unique += i

print(unique)