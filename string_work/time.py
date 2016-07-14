import datetime
y, d, h = [int(i) for i in input().split()]
n = int(input())
t = datetime.date(y, d, h) + datetime.timedelta(n)
for i in str(t).split("-"):
    print(int(i), end=" ")