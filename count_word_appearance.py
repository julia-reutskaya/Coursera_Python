in_data = open('input.txt').read()
list_data = in_data.split()
words_dict = dict()
list_count = []
for i in list_data:
    if i not in words_dict:
        words_dict[i] = words_dict.get(i, -1) + 1
        list_count.append(0)
    else:
        words_dict[i] += 1
        list_count.append(int(words_dict[i]))
print(*list_count)
