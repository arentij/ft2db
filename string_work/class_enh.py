n = int(input())
a = {}
for i in range(n):
    s = input().split(":")
    a[s[0]] = s[1].split()

print(a)

m = int(input())
for j in range(m):

    if j in a.keys():
        print("Yes")
    else:
        print("No")
