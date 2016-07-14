import re
pattern = r"19\d{9}"
string = input()
if re.match(pattern, string) and len(string) == 11:
    print("Yes")
else:
    print("No")
