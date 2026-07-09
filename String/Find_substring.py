

# find all substring in a string 

str1 = "abc"

len_str = len(str1)

for i in range(len_str):
    for j in range(i+1, len_str+1):
        print(str1[i:j])
