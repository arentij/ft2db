def mod_checker(x, mod=0):
    return lambda y: y % x == mod

f3 = mod_checker(3)
f4 = mod_checker(4)

print(f3(3))
print(f4(3))
print(f3(12))
