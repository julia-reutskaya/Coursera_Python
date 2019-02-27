num_list = list(map(int, input().split()))
max_val = max(num_list)
min_val = min(num_list)
max_index = num_list.index(max_val)
min_index = num_list.index(min_val)
num_list[min_index] = max_val
num_list[max_index] = min_val
print(' '.join(map(str, num_list)))
