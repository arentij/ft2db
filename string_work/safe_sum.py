def sum(a, b):
    if type(a) == type(b) == int:
        if a > 0 and b > 0:
            return int(a) + int(b)
        else:
            raise ValueError
    else:
        raise TypeError
print(sum(-1.1, 2.1))

