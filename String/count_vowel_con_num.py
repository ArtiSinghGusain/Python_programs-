# 8.	Count vowels, consonants, digits, and spaces in a string. Done
from String.remove_vowels import vowels

str1 = "PythonProgramming 123"

digit = 0
vowel = 0
consonant = 0
spaces = 0

vowels = "AEIOUaeiou"

for i in str1:
    if i in vowels:
        vowel += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        spaces += 1
    else:
        consonant += 1

print(digit,spaces,consonant,vowel)

