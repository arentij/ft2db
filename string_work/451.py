import sys
import re
data = sys.stdin.readlines()
pattern = r"[^a-zA-Z0-9 ]"
for line in data:
    print(re.sub(pattern, "", line), end=" ")

