lst = [int(i) for i in input().split()]
n = len(lst)
ablst = [abs(lst[i]-lst[i+1]) for i in range(n-1)]
numbers = [i+1 for i in range(n-1)]

if len(lst) == 1:
    print("Jolly")
else:
    flag = True
    for i in range(n-1):
        if sorted(ablst)[i] == i+1:
            continue
        else:
            flag = False
            break
    if flag:
        print("Jolly")
    else:
        print('Not jolly')



    '''
    if all(i in ablst for i in numbers):
        print("Jolly")
    else:
        print("Not jolly")
    '''