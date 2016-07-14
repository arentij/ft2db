def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

x_1, y_1, x_2, y_2 = float(input()), float(input()), float(input()), float(input())
print(distance(x_1, y_1, x_2, y_2))
