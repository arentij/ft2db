import re
n, m = [int(i) for i in input().split()]
cinema = []
for i in range(n):
    cinema.append('')
    for j in input().split():
        cinema[i] += str(j)
k = int(input())
a = 0
pattern = r'0'*k
for i in range(n):
    if re.search(pattern, cinema[i]) is None:
        continue
    else:
        a = i + 1
        break
print(a)