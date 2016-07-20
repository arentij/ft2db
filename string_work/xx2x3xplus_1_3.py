def back(x):
    if x % 6 == 0:
        return [x-1, x // 2, x // 3]
    elif x % 3 == 0:
        return [x-1, x // 3]
    elif x % 2 == 0:
        return [x-1, x // 2]
    else:
        return [x-1]

v = int(input())
d = {v: back(v)}
v_values = []
to_check = [v]
to_check2 = []
n = 0
while 1 not in to_check:

    for y in to_check:
        d[y] = back(y)
        to_check2.extend(filter(lambda x: x not in v_values, back(y)))

    to_check.clear()
    to_check = to_check2.copy()
    to_check2.clear()
    n += 1
    # print(to_check)
    # input()

print(n)
print(d)
print("finding the way")

k = 1
while k != v:
    print("looking for key where is k=", k)
    for ke in d.keys():
        # print(ke)
        if k in d[ke]:
            print(k, end=" ")
            k = ke
            break
        else:
            # print("not here")
            input()










