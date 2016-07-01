def wow(x, y):
    print(x//y, end=" ")
    if x % y != 0:
        return wow(y, x % y)


n, m = [int(i) for i in input().split("/")]
if m == 0:
    print('None')
else:
    wow(n, m)
