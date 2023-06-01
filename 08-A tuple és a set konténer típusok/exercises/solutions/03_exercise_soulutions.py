# 3.
def tuple_ops(t1, t2):
    summa = t1[0] + t2[0]
    diff = t1[0] - t2[0]
    prod = t1[0] * t2[0]
    return (summa, diff, prod)


print(tuple_ops((3, 5), (4, 2)))
