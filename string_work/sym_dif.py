a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])
c = a.symmetric_difference(b)
print(*c)

