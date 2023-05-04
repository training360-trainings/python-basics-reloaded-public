# 2.
my_list = [1, 2, 3, 4, 5, 2, 3]
uniqe_list = []

for i in my_list:
    if i not in uniqe_list:
        uniqe_list.append(i)

print(uniqe_list)
