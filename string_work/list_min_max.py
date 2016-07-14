a = [int(i) for i in input().split()]
mi = a[0]
ma = a[0]
for i in a:
    if i > ma:
        ma = i
    if i < mi:
        mi = i
print(ma, mi)
