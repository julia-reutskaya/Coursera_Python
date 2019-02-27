in_data = open('input.txt', encoding='utf8')
words_dict = {}
list_words = list()
for line in in_data:
    words_list = line.strip().split()
    for word in words_list:
        words_dict[word] = words_dict.get(word, 0) + 1
for item in words_dict:
    list_words.append((words_dict[item], item))
list_words.sort(key=lambda x: (-x[0], x[1]))
i = 0
res = list()
for list_words[i] in list_words:
    word = list_words[i]
    print(word[1])
    i += 1
