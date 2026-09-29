
numbers = [1,2,[3,4],6,[8,9]]

flatten_list = []

for item in numbers:
    if isinstance(item,list):
            flatten_list.extend(item)
    else:
        flatten_list.append(item)

print(flatten_list)