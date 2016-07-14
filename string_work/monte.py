import random

number = 200000
goods = 0
bads = 0
for i in range(number):

    c = []
    k = 15
    for j in range(k):
        c.append((-1) ** (random.randint(1, 2)))

    s = 0
    flag = True

    for a in c:
        s += a
        if s < 0:
            flag = False
            break


    if flag:
        # print("good")
        goods += 1
        # print(c, " s=", s)
    else:
        # print("bad")
        bads += 1

print("good: ", goods)
print("bads: ", bads)
print("P = ", goods/(goods+bads))