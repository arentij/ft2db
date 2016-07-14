from bisect import insort
n = int(input())
a = [0]
m = 0
for i in range(n):
    s = input()
    if s == "ExtractMax":
        print(a[-1])
        a.pop()

    else:
        k = int(s.split()[1])
        insort(a, k)
