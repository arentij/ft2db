font = " abcdefghijklmnopqrstuvwxyz"
k = int(input())
crypt = {}
l = len(font)
for i in range(l):
    crypt[font[i]] = font[(i + k) % l]
inp = input()
print("Result: \"", end="")
for s in inp.strip():
    print(crypt[s], end="")
print("\"")