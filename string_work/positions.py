a = [int(i) for i in input().split()]
n = int(input())
r = []
for i in range(len(a)):
    if a[i] == n:
        r.append(i)
if r:
    print(*r)
else:
    print("Missing")
