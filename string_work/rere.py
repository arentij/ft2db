import re, sys
pattern = r"you|You"
n = 0
for string in sys.stdin:
    n += int(len(re.findall(pattern, string)))
    print(n, end=" ")
