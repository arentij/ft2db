n, m, k = int(input()), int(input()), int(input())
variants = []
for i in range(n):
    for j in range(m):
        variants.append((i+1)*(j+1))
print(variants)
if k in variants:
    print("Yes")
else:
    print("No")
