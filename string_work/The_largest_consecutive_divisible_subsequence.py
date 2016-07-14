def rec(x, m=0):
    if d[x]:
        m += 1
        ml = []
        for dx in d[x]:
            ml.append(rec(dx, m))
        return max(ml)
    else:
        return m+1


a = [2, 3, 4, 4, 5, 6, 600, 8, 20, 32, 64]
a = list(set(a))
a.sort()
n = len(a)
M = [[0 for j in range(n)] for i in range(n)]
d = {x: [] for x in a}

d2 = [[x, d[x]] for x in a]


for i in range(n):
    for j in range(i+1, n):
        if a[j] % a[i] == 0:
            M[i][j] = 1
            d[a[j]].append(a[i])


print("  ", end="")
print(*a, sep=" ")
for i in range(n):
    print(a[i], end=r" ")
    print(*M[i])



