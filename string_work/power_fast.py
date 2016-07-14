def power(a, n):
    if n % 2 == 0:
        return (a**2)**(n//2)
    else:
        return a*power(a, n-1)


a0, n0 = float(input()), int(input())
print(power(a0, n0))
