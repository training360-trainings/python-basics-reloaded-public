# 8.
def alphabetical_set(s):
    return {w for w in s if sorted(w) == list(w)}


words = {'banana', 'cat', 'dog', 'abc'}
print(alphabetical_set(words))
