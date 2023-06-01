# 6.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = []

for i, num in enumerate(list1):
    if i % 2 != 0:
        result.append(list2[i-1])
    else:
        result.append(num)

print(result)
