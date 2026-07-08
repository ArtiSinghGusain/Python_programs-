# 6.	Remove vowels from string. Done

str1 = "PythOn Programming"

vowels = "AEIOUaeiou"
result = ""

for i in str1.replace(" ",""):
    if i not in vowels:
        result += i

print(result)