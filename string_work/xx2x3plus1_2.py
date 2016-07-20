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
d = {0: [v]}
v_values = [v]
i = 0
parent = {}

flag = True
while flag:
    if v == 1:
        break
    d[i+1] = []
    for r in d[i]:
        if r % 3 == 0 and r // 3 not in v_values:
            d[i+1].append(r // 3)
            v_values.append(r // 3)
            if r // 3 == 1:
                flag = False
        if r % 2 == 0 and r // 2 not in v_values:
            d[i+1].append(r // 2)
            v_values.append(r // 2)
            if r // 2 == 1:
                flag = False
        if r - 1 not in v_values:
            d[i+1].append(r-1)
            v_values.append(r-1)
    i += 1
    # print(i, d)
d[i] = [1]
print(i)
print(d)

