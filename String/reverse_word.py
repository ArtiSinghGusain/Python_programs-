#Reverse a word in python 

str1 = "I love Python"

reverse_word_list = []
list_str = str1.split()
list_str.reverse()

for i in list_str:

    reverse_word_list.append(i)

print(reverse_word_list)

rev_word = " ".join(reverse_word_list)

print(rev_word)


