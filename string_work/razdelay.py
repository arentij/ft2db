x = int(input())
a = [int(i) for i in input().split()]
l = len(a)
r = {x: 0 for x in set(a)}
for i in a:
    r[i] += 1

if max(r.values()) > l // 3:
    print(1)
else:
    print(0)
