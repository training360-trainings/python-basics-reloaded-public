# Dictionary is a collection which is ordered ** and changeable. No duplicate members.

user_dict = {'name': 'John Doe', 'age': 33}


print('keys:', user_dict.keys())
for i in user_dict.keys():
    print(i)

print('values:', user_dict.values())
for i in user_dict.values():
    print(i)

print('items:', user_dict.items())
for i in user_dict.items():
    print(i)
    print(i[0], i[1])

for i, v in user_dict.items():
    print(i, v)
