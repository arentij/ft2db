word_counter = {}

with open('dataset_28252_1.txt') as inf:
    for line in inf:
        for word in line.split():
            word = word.lower()
            if word in word_counter.keys():
                word_counter[word] += 1
            else:
                word_counter[word] = 1
print(sorted(word_counter.values()))
max_n = max(word_counter.values())
max_n_keys = [i for i in word_counter.keys() if word_counter[i] == max_n]
print(sorted(max_n_keys), max_n)

