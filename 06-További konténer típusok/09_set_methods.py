# https://realpython.com/python-sets/
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# https://realpython.com/python-sets/

# add() - elem hozzáadása
# update() - elemek hozzáadása, a apamreméter egy másik set, list lehet
# remove() - érték eltávolítása, errort dob ha nincs
# discard() - érték eltávolítása, nem dob errort ha nincs
# union()
# intersection()
# difference()
# frozenset() - immutable-é teszi a set-et
# issuperset()
# issubset()

# unió
x1 = {'a', 'b', 'c'}
x2 = {'b', 'c', 'd'}
x1.union(x2)

# metszet
x1.intersection(x2)

# különbség
x1.difference(x2)

# symmetric_difference
# return the set of all elements in either x1 or x2, but not both
x1.symmetric_difference(x2)

# isdisjoint
# returns True if x1 and x2 have no elements in common
{'b'}.isdisjoint(x2)

# issubset
# Determine whether one set is a subset of the other.
x1.issubset({'a', 'b', 'c', 'd'})

# x1 > x2 returns True if x1 is a proper superset of x2:
# x1 = {'foo', 'bar', 'baz'}
# x2 = {'foo', 'bar'}
# x1 > x2

x1.issuperset({'foo', 'bar'})
