n = int(input())
a = [[abs(i-j) for i in range(n)] for j in range(n)]
for i in range(n):
    print(*a[i])

