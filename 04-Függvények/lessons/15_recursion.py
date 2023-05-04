# Legnagyobb közös osztó

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(11, 33))
