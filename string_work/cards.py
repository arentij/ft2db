chain = {"6": 0, "7": 1, "8": 2, "9": 3, "10": 4, "J": 5, "Q": 6, "K": 7, "A": 8}

c1, c2 = [i for i in input().split()]
trump = input()

if c1[-1] == c2[-1]:
    if chain[c1[:-1]] > chain[c2[:-1]]:
        print("First")
    elif chain[c1[:-1]] < chain[c2[:-1]]:
        print("Second")
    else:
        print("Error")
elif c1[-1] == trump:
    print("First")
elif c2[-1] == trump:
    print("Second")
else:
    print("Error")
