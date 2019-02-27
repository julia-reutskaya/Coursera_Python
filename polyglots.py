one_lang = set()
all_lang = set()
for i in range(int(input())):
    lang_count = int(input())
    lang = {input() for j in range(lang_count)}
    all_lang.update(lang)
    if i == 1:
        one_lang.update(lang)
    else:
        one_lang &= lang
print(len(one_lang))
print('\n'.join(sorted(one_lang)))
print(len(all_lang))
print('\n'.join(sorted(all_lang)))
