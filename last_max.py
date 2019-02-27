num_list = list(map(int, input().split()))
max_num = num_list[0]
index = 0
index1 = 0
for i in num_list:
    index += 1
    if i >= max_num:
        max_num = i
        index1 = index - 1
print(max_num, index1)
