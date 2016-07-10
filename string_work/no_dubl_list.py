def f(ls):
# return (list(set(ls))) - easier
    a = []
    for i in ls:
        if i not in a:
            a.append(i)
    return a

l = [int(i) for i in input().split()]

print(f(l))
