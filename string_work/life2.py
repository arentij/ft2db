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
        neighbors = []
        for di in range(-1, 2):
            for dj in range(-1, 2):

                if di == 0 and dj == 0:
                    continue

                x = (i + di + n) % n
                y = (j + dj + m) % m

                if A[x][y] == "X" and not [x, y] in neighbors:
                    s += 1
                    neighbors.append([x, y])
        if A[i][j] == "X" and (s == 2 or s == 3):
            B[i][j] = "X"
        elif A[i][j] == "." and s == 3:
            B[i][j] = "X"
        else:
            B[i][j] = "."

printing(B)
