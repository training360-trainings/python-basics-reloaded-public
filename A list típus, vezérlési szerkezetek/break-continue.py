brands = ['Microsoft', 'Apple', 'Alphabet', 'Amazon', 'Meta']
search = 'Alphabet'

for i in brands:
    if i in brands:
        print('ok')
        break

print('Found' if search in brands else 'Not found')
