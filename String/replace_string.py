# Replace space in a string with "-"

str1 = "Python programming"

new_str = str1.replace(" ","_")

print(new_str)


#2nd Method

replaced_str = ""
for i in str1:
    if i == " ":
        i = "_"
    replaced_str += i

print(replaced_str)

