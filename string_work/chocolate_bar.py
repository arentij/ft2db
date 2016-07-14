n, m, k = int(input()), int(input()), int(input())
variants = []

for i in range(n//2):
    variants.append(m*(i+1))
    variants.append(m*(n-1-i))
print()
for i in range(m//2):
    variants.append(n*(i+1))
    variants.append(n*(m-1-i))

if k in variants:
    print("Yes")
else:
    print("No")
