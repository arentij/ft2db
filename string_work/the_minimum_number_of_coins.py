n, m = [int(i) for i in input().split()]
a = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    a[i] = [int(x) for x in input().split()]

for i in range(n):
    for j in range(m):
        if i == j == 0:
            a[i][j] = a[i][j]
        elif i == 0:
            a[i][j] += a[i][j-1]
        elif j == 0:
            a[i][j] += a[i-1][j]
        else:
            a[i][j] += min(a[i][j-1], a[i-1][j])

print(a[n-1][m-1])

