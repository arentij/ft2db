with open('dataset_28255_1.txt') as inf, open("text_copy.txt", "w") as ouf:
    a = []
    for line in inf:
        a.append(line)
    for line in a[::-1]:
        ouf.write(line)


