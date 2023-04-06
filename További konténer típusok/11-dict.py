# Dictionary is a collection which is ordered ** and changeable. No duplicate members.

user_dict = {'name': 'John Doe', 'age': 33}

print(user_dict['name'])

user_dict['age'] = 18
print(user_dict)

user_dict['job'] = 'mentor'
print(user_dict)

user_dict.pop('name')
print(user_dict)

user_dict['job'] = 'teacher'
print(user_dict)

user_dict.update({'job': 'frontend dev'})
print(user_dict)

user_dict.update({'job': 'python dev', 'salary': 70000})
print(user_dict)
