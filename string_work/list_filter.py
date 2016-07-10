def filter_positive(l):
    return list(filter(lambda x: x > 0, l))

print(filter_positive([0, 1, -1, 2, -3, 56, -12]))


def filter_positive2(l):
    return [int(i) for i in l if int(i) >= 0]
