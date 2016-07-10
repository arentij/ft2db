a, b, c, d, e, f = float(input()), float(input()), float(input()), float(input()), float(input()), float(input())

if a == b == c == d == 0:
    if e == f == 0:
        print("5")
    else:
        print("0")
elif a == c == 0:
    if (b == 0 and e != 0) or (d == 0 and f != 0):
        print("0")
    elif b != 0 and d == f == 0:
        y0 = e/b
        print("4", y0)
    elif d != 0 and b == e == 0:
        y0 = f/d
        print("4", y0)
    else:
        y0 = e/b
        if d*e/b == f:
            print("4", y0)
        else:
            print("0")
elif b == d == 0:
    if (a == 0 and e != 0) or (c == 0 and f != 0):
        print("0")
    elif a != 0:
        x0 = e/a
        if c*x0 == f:
            print("3", x0)
        else:
            print("0")
    elif c != 0:
        x0 = f/c
        if a*x0 == e:
            print("3", x0)
        else:
            print("0")
    else:
        if e*c == a*f:
            x0 = e/a
            print("3", x0)
elif a == d == 0:
    x0 = f/c
    y0 = e/b
    print("2", x0, y0)
elif b == c == 0:
    x0 = e/a
    y0 = f/d
    print("2", x0, y0)
elif a*d == c*b:
    if b*f == e*d:
        if b != 0:
            k1 = -a/b
            k2 = e/b

        elif d != 0:
            k1 = -c/d
            k2 = f/d
        print("1", k1, k2)
    else:
        print("0")
else:
    y0 = (c*e-f*a)/(b*c-a*d)
    x0 = (e-b*y0)/a
    print("2", x0, y0)
