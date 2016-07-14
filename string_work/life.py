def printing(o):
    for i2 in range(n):
        for j2 in range(m):
            print(o[i2][j2], end="")
        print()
    print()


n, m = [int(i) for i in input().split()]
A = ['.']*n
for i in range(n):
    A[i] = input()
B = [['.' for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        s = 0
        for di in range(-1, 2):
            for dj in range(-1, 2):
                x = (i + di)
                y = (j + dj)
                if x == n:
                    x = 0
                if y == m:
                    y = 0
                if x == i and y == j:
                    continue
                if A[x][y] == "X":
                    s += 1
        if A[i][j] == "." and s == 3:
            B[i][j] = "X"
        elif A[i][j] == "X" and (s == 2 or s == 3):
            B[i][j] = "X"
        else:
            B[i][j] = "."

printing(B)

