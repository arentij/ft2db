n = int(input())
d = []
e = []
for i in range(n):
    d.append(input().lower())

m = int(input())
for j in range(m):
    for word in input().split():
        if word.lower() not in d and word.lower() not in e:
            print(word.lower())
            e.append(word.lower())

