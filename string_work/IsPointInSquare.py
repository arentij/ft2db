def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


x0, y0 = float(input()), float(input())
if IsPointInSquare(x0, y0):
    print("YES")
else:
    print("NO")