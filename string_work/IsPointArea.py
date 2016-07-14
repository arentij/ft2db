def IsPointInArea(x, y):
    return (x+1)**2 + (y-1)**2 <= 4 and y >= -1*x and y >= 2*x + 2 or (
            (x+1)**2 + (y-1)**2 >= 4 and y <= -1*x and y <= 2*x + 2
    )

x1, y1 = float(input()), float(input())
if IsPointInArea(x1, y1):
    print("YES")
else:
    print("NO")
