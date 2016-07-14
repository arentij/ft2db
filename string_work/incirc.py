def IsPointInCircle(x, y, xc, yc, r):
    return (xc-x)**2 + (y-yc)**2 <= r**2

x1, y1, xc1, yc1, r1 = float(input()), float(input()), float(input()), float(input()), float(input())
if IsPointInCircle(x1, y1, xc1, yc1, r1):
    print("YES")
else:
    print("NO")
