def printing(x):
    for i2 in range(n):
        for j2 in range(m):
            print(x[i2][j2], end="")
        print()
    print()

n, m = [int(i) for i in input().split()]
A = ['']*n
for i in range(n):
    A[i] = input()
B = [['*' for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        s = 0
        if A[i][j] == ".":

            for di in range(-1, 2):
                if i+di < 0 or i+di >= n:
                    continue
                for dj in range(-1, 2):
                    if j+dj < 0 or j+dj >= m:
                        continue
                    if A[i+di][j+dj] == "*":
                        s += 1
            B[i][j] = str(s)

printing(B)