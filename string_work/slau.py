a, b, c, d, e, f = [float(i) for i in input().split()]
# ax + by = e
# cx + dy = f
print(r'{}x + {}y = {}'.format(a, b, e))
print(r'{}x + {}y = {}'.format(c, d, f))
if a == b == c == d == 0:
    if e == f == 0:
        print("everywhere")
    else:
        print("no solution")
elif a == c == 0:
    if (b == 0 and e != 0) or (d == 0 and f != 0):
        print("no solution")
    elif b != 0 and d == f == 0:
        y0 = e/b
        print("any x and y0=", y0)
    elif d != 0 and b == e == 0:
        y0 = f/d
        print("any x and y0=", y0)
    else:
        y0 = e/b
        if d*e/b == f:
            print("any x and y0=", y0)
        else:
            print("no solution")
elif b == d == 0:
    if (a == 0 and e != 0) or (c == 0 and f != 0):
        print("No solution")
    elif a != 0:
        x0 = e/a
        if c*x0 == f:
            print("any y and x0=", x0)
        else:
            print("No solution")
    elif c != 0:
        x0 = f/c
        if a*x0 == e:
            print("any y and x0=", x0)
        else:
            print("No solution")
elif a == d == 0:
    x0 = f/c
    y0 = e/b
    print("x=", x0, "y=", y0)
elif b == c == 0:
    x0 = e/a
    y0 = f/d
    print("x=", x0, "y=", y0)
elif a*d == c*b and b*f == e*d:
    k1 = -a/b
    k2 = e/b
    print("line k=", k1, "b=", k2)

else:
    y0 = (c*e-f*a)/(b*c-a*d)
    x0 = (e-b*y0)/a
    print("solution: x0=", x0, "y0=", y0)

# ax + by = e
# cx + dy = f
