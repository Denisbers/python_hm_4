my_list = [0, 1, 0, 12, 3]

for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] == 0:
        my_list.append(my_list.pop(i))
print(my_list)