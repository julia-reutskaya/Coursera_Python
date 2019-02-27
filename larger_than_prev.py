num_list = list(map(int, input().split()))
largest_next = []
for i in range(1, len(num_list)):
    current_num = int(num_list[i])
    prev_num = int(num_list[i - 1])
    if current_num > prev_num:
        largest_next.append(current_num)
print(' '.join(map(str, largest_next)))
