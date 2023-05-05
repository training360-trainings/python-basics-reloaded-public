# 5.
import list_handling

my_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
unique_list = list_handling.remove_duplicates(my_list)
sorted_list = list_handling.sort_descending(unique_list)

print('Original list:', my_list)
print('Unique list:', unique_list)
print('Sorted list:', sorted_list)
