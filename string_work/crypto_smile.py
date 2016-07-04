crypt = {}
k = int(input())
string = input()
# for i in range(72):
#   crypt[chr(128591 + i)] = chr(128591+(i+k) % 73)
# print(ord(chr(128591 + i)), ord(chr(128591 + (k+i) % 73)))
for i in string:
    print(chr(128591 + ((ord(i)+k) % 128591) % 72), end="")

