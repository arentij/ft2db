import operator as op
n, v = [int(i) for i in input().split()]
items = []
for i in range(n):
    item = [int(i) for i in input().split()]
    item.append(item[0]/item[1])
    items.append(item)

items.sort(key=op.itemgetter(-1), reverse=True)

price = 0
f = v

for i in items:
    if i[1] <= f:
        f -= i[1]
        price += i[0]
    else:
        price += i[0]*f/i[1]
        f = 0
        break

print(price)
