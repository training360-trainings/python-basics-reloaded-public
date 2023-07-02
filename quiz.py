text = "Python"
a, *b, c = text
result = f"{a}-{c}-{''.join(b)}"
print(result)
