def modify_list(l):
    for i in range(len(l)):
        if l[0] % 2 == 0:
            l.append(l[0]//2)
        l.pop(0)


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)