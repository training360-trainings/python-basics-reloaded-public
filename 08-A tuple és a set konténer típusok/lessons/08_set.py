# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# https://realpython.com/python-sets/

# add() - elem hozzáadása
# update() - elemek hozzáadása, a pamreméter egy másik set, list, tuple lehet
# remove() - érték eltávolítása, errort dob ha nincs
# discard() - érték eltávolítása, nem dob errort ha nincs
# union()
# intersection()
# difference()
# frozenset() - immutable-é teszi a set-et
# issuperset()
# issubset()

my_set = {1, 2, 3}
print('set:', my_set)
# TypeError
# print('first element:', my_set[0])

my_set.add(4)
print('set:', my_set)

my_set.update([5, 6, 7])
print('set:', my_set)

# update, works with sets
my_set |= {5, 6, 7}
print('set:', my_set)

my_set.remove(4)
print('set:', my_set)

# not raised exception
my_set.discard(2)
print('set:', my_set)

# remove a random element
my_set.pop()
print('set:', my_set)
