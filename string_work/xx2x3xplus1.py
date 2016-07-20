def x2x3xp1(y):
    return [2*y, 3*y, y+1]

x = int(input())
d = {0: [1]}
i = 0
values = [1]
way = [x]
while x not in values:
    d[i+1] = []
    for z in d[i]:
        for r in x2x3xp1(z):
            if r not in values and r <= x:
                d[i+1].append(r)
                values.append(r)
    i += 1

print(i)
p = x
while p != 1:
    if p-1 in d[i-1]:
        way.append(p-1)
        p -= 1
        i -= 1
    elif p % 2 == 0 and p // 2 in d[i-1]:
        way.append(p//2)
        p //= 2
        i -= 1
    elif p % 3 == 0 and p // 3 in d[i-1]:
        way.append(p//3)
        p //= 3
        i -= 1

print(*way[::-1])
