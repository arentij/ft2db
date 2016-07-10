def longest_row(s):
    l = [s[0]]
    m = s[0]
    for j in range(1, len(s)):
        if int(s[j]) > m:
            m = int(s[j])
            l.append(m)
    return l

string_list = [int(i) for i in input().split()]
ml = 0
for i in range(len(string_list)):
    if len(string_list[i:]) < ml:
        break
    elif len(longest_row(string_list[i:])) > ml:
        a = longest_row(string_list[i:])
        ml = len(a)
print(*a)
