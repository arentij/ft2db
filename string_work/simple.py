n = int(input())
flag = False
if n % 400 == 0:
    flag = True
elif n % 100 == 0:
    flag = False
elif n % 4 == 0:
    flag = True
if flag:
    print("Leap")
else:
    print("Regular")
