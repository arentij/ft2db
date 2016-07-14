import re


def number_sub(st, at, bt, n=0):
    if re.search(at, st):
        n += 1
        st = re.sub(at, bt, st)
        try:
            return number_sub(st, at, bt, n)
        except RuntimeError:
            return "Impossible"
    return n
s, a, b = input(), input(), input()

print(number_sub(s, a, b))
