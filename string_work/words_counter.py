s = input().lower().split()
d = {x: 0 for x in set(s)}
for word in s:
    d[word] += 1
for i in d.keys():
    print(d[i], i)

