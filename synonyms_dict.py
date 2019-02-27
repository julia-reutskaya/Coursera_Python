words_dict = {}
for i in range(int(input())):
    list_words = (input()).split()
    words_dict[list_words[0]] = words_dict.get(list_words[0], list_words[1])
    words_dict[list_words[1]] = words_dict.get(list_words[1], list_words[0])
print(words_dict[input()])
