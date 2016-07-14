def printing(x):
    for i2 in range(n):
        for j2 in range(m):
            print(x[i2][j2], end="")
        print()
    print()


n, m = [int(i) for i in input().split()]
A = ['.']*n
for i in range(n):
    A[i] = input()
B = [['.' for j in range(m)] for i in range(n)]
M = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if A[i][j] == "X":

            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if dj == di == 0:
                        continue
                    x1 = (i + di + n) % n
                    y1 = (j + dj + m) % m
                    M[x1][y1] += 1

# printing(M)

for i in range(n):
    for j in range(m):
        if A[i][j] == "." and M[i][j] == 3:
            B[i][j] = "X"
        elif A[i][j] == "X" and M[i][j] in [2, 3]:
            B[i][j] = "X"

printing(B)

