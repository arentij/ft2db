import re

# match search findall sub
pattern = r"0{2}"
string = "1001"
match_object = re.match(pattern, string)
search_object = re.search(pattern, string)
findall_object = re.findall(pattern, string)
sub_object = re.sub(pattern, "replaced", string)

print(match_object)
print(search_object)
print(sub_object)

print(findall_object)
