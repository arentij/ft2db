def summa(x, s=0):
    a = s
    if x == 0:
        return a
    else:
        a += x
        return summa(int(input()), a)


print(summa(int(input())))
