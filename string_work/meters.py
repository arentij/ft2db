n, unit_from, word, unit_to = [i for i in input().split()]
n = float(n)
coeff = {"mile": 1609, "yard": 0.9144, "m": 1, "foot": 0.3048, "inch": 0.0254, "km": 1000, "cm": 0.01, "mm": 0.001}
a = n*coeff[unit_from]/coeff[unit_to]
print("%.2e" % a)
