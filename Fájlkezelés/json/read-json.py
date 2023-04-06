from email.policy import default
from json import load

json_file = open(file='./MOCK_DATA.json', mode='r', encoding='utf-8')
json_data = load(json_file)
# print(type(json_data))
users = json_data['users']
# print(type(users))


def generate_id():
    return max(list(map(lambda user: user['id'], users))) + 1


def get_all_users():
    return users


def find_user_index(id):
    return users.index(find_user(id))


def find_user(id):
    return next((user for user in users if user['id'] == id), None)
    # return ([user for user in users if user['id'] == id] or [None])[0]
    # return (list(filter(lambda user: user['id'] == id, users)) or [None])[0]


def update_user(id, updated_user):
    index = find_user_index(id)
    users[index].update(updated_user)
    return users[index]


def create_user(user):
    user.update({id: generate_id()})
    users.append(user)
    return user


def remove_user(id):
    user = find_user(id)
    users.remove(user)


print(find_user_index(2000))
# print(find_user(2))
# print(update_user(1, {'first_name': 'Gergely', 'last_name': 'Gáll'}))
# remove_user(1)
# print(find_user(1))
