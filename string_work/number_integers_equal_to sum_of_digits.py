def sum_dig(x):
    x = str(x)
    s1 = 0
    for i1 in x:
        s1 += int(i1)
    return s1

n = int(input())
s = 0
n1 = sum_dig(n)
for i in range(1,n):
    if sum_dig(i) == n1:
        s += 1
print(s)
