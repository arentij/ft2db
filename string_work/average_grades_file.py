n = 0
a = [0, 0, 0]
with open('dataset_28252_1.txt') as inf:
    for line in inf:
        n += 1
        st = line.strip().split(";")
        av = 0
        for i in range(3):
            a[i] += int(st[i+1])
            av += int(st[i+1])
        av /= 3.0
        print(av)
for i in range(3):
    print(a[i]/n, end=" ")
