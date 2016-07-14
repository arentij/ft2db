import re
string = "MCMLXXXIV"
pattern = r"IV|IX|XL|XC|CD|CM|I|V|X|L|C|D|M"
rules = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
         "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
s = 0
for i in re.findall(pattern, string):
    s += rules[i]
print(s)

