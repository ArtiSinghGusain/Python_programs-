# 1.	Reverse a string (different ways: slicing, loop, recursion). - Done

st = "Python"

reverse_string = ""

for i in st:
    reverse_string = i+reverse_string

print(reverse_string)


#2nd way to do it by slicing

st = "python"

reverse_st = st[::-1]
print(reverse_st)

