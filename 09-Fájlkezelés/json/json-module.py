from json import loads, dumps

json = '''{
    'firstName': 'John',
    'lastName': 'Smith',
    'phoneNumbers': [
        {
            'type': 'home',
            'number': '212 555-1234'
        },
        {
            'type': 'office',
            'number': '646 555-4567'
        }
    ]
}'''

john = loads(json)
print(type(john), john)
print(john['phoneNumbers'][0]['number'])

python_code = {'name': 'Gáll Gergely', 'age': 38}
print(type(dumps(python_code)))
