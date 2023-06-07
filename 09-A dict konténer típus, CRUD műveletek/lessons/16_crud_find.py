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


def find_user(id):
    for user in users:
        if user['id'] == id:
            return user
    return None


print(find_user(10))
