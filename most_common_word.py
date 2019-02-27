in_data = open('input.txt', encoding='utf8')
words_dict = {}
for line in in_data:
    words_list = line.strip().split()
    for word in words_list:
        words_dict[word] = words_dict.get(word, 0) + 1
print(sorted(words_dict.items(), key=lambda x: (-x[1], x[0]))[0][0])
