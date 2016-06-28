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

for i in range(n):
    for j in range(m):
        s = 0
        neigh = []
        print(i, j)
        for di in range(-1, 2):
            for dj in range(-1, 2):
                x = (i + di)
                y = (j + dj)
                if x == n:
                    x = 0
                if y == m:
                    y = 0
                if x == -1:
                    x = n - 1
                if y == -1:
                    y = m - 1
                if x == i and y == j:
                    print("OLOLO")
                    continue
                if A[x][y] == "X":
                    if [x, y] in neigh:
                        continue
                    else:
                        s += 1
                        neigh.append([x, y])
                print(x, y)
        print(s, neigh)
        print()
        if A[i][j] == "." and s == 3:
            B[i][j] = "X"
        elif A[i][j] == "X" and (s == 2 or s == 3):
            B[i][j] = "X"
        else:
            B[i][j] = "."

printing(B)

