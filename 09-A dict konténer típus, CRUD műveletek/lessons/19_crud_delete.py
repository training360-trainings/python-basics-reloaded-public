users = [
    {
        'id': 1,
        'first_name': 'Suzie',
        'last_name': 'Sherland',
        'email': 'ssherland0@alibaba.com',
    },
    {
        'id': 2,
        'first_name': 'Morty',
        'last_name': 'Biddwell',
        'email': 'mbiddwell1@telegraph.co.uk',

    },
    {
        'id': 3,
        'first_name': 'Madelon',
        'last_name': 'Feares',
        'email': 'mfeares2@cmu.edu',

    }
]


def get_all_users():
    return users


def find_user(id):
    for user in users:
        if user['id'] == id:
            return user
    return None


def update_user(id, updated_user):
    index = users.index(find_user(id))
    if index is not None:
        users[index].update(updated_user)
    return users[index]


def create_user(user):
    user.update({'id': users[-1]['id'] + 1})
    users.append(user)
    return user


def remove_user(id):
    user = find_user(id)
    users.remove(user)


# print(find_user(2))
# print(update_user(1, {'first_name': 'Gergely', 'last_name': 'Gáll'}))
# print(create_user({'first_name': 'Johnny', 'last_name': 'Boy'}))
remove_user(1)
print(find_user(1))
