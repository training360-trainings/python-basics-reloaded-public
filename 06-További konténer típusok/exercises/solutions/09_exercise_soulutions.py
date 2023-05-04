# 9.
def common_elements(lst1, lst2):
    return list(set(lst1).intersection(lst2))


lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
print(common_elements(lst1, lst2))
