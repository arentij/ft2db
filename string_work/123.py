def modify_list(l):
    a = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            a.append(l[i]//2)
    l.clear()
    l.extend(a)
li = [1, 2, 3, 4, 5, 6]
print(li)
modify_list(li)
print(li)
