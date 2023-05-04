# 10.
def find_duplicates(lst):
    duplicates = set()
    seen = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates


print(find_duplicates([1, 2, 3, 2, 4, 3]))
