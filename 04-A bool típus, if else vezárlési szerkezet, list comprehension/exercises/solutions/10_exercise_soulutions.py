# 10.
n = int(input('Adj meg egy számot: '))
i = 1

while i <= n:
    if n % i == 0:
        print(i)
    i += 1
