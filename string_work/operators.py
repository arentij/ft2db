n = int(input())
sett = []
a = n
sett.append(a)
while a != 1:
    if a % 2 == 0:
        a /= 2
    else:
        a = 3*a + 1
    sett.append(a)
for i in sett:
    print(int(i), end=" ")
