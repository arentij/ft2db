def modify_list(l):
    l = [x//2 for x in l if x % 2 == 0]
    return

s = [1, 2, 3, 4, 5, 0,6, 7, 8]
modify_list(s)
print(s)


a = [1, 2, 3, 4, 5, 6]
a = [x//2 for x in a if x % 2 == 0]
b = [i//2 for i in filter(lambda x: x % 2 == 0, a)]
print(b)
print(a)

