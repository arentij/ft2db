string = input().split()
result = {}
for i in string:
    if len(i) in result.keys():
        result[len(i)] += 1
    else:
        result[len(i)] = 1
for i in sorted(result.keys()):
    print(i, ': ', result[i], sep="")
