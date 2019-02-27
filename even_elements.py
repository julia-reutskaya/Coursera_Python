num_list = list(map(int, input().split()))
even_num = []
for i in num_list:
    if i % 2 == 0:
        even_num.append(i)
print(' '.join(map(str, even_num)))
