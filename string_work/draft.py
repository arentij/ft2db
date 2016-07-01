setup = [1, 2, 3, 4]
setup2 = [1, 2]

if all(i in setup for i in setup2):
    print("Yes")