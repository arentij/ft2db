a, b = [int(i) for i in input().split()]
Matrix = [[0]*b]*a

for i in range(a):
    Matrix[i] = [int(j) for j in input().split()]

for j in range(b):
    for i in range(a):
        print(Matrix[i][j], sep=" ", end=" ")
    print()
