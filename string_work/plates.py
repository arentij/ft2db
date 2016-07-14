import re
pattern = r"[ABEKMHOPCTYX]\d\d\d[ABEKMHOPCTYX][ABEKMHOPCTYX]"
string = input()
if re.match(pattern, string) and len(string) == 6:
    print("Yes")
else:
    print("No")
