def modify(x, y):
    return (x+y)*113 % 10000007

n = int(input())
l = [int(i) for i in input().split()]
checksum = 0
for i in range(n):
    checksum = modify(checksum, l[i])

print(checksum)
