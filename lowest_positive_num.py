num_list = list(map(int, input().split()))
pos_num = []
for i in num_list:
    if i > 0:
        pos_num.append(i)
print(min(pos_num))
