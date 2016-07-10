login = 123
password = 321


def logging(x, y):
    if x == login:
        if y == password:
            print("Login success")
        else:
            print("Wrong password")
    else:
        print("No user with login {} found".format(x))

l, p = [int(i) for i in input().split()]
logging(l, p)

