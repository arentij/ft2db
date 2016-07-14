import re
string = input()
pattern = r"\d+\D|\D"
for i in re.findall(pattern, string):
    if len(i) == 1:
        print(i, end="")
    else:
        print(i[-1]*int(i[0:-1]), end="")