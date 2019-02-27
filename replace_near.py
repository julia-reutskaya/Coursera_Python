num_list = list(map(int, input().split()))
for i in range(1, len(num_list), 2):
    num_list[i - 1], num_list[i] = num_list[i], num_list[i - 1]
print(' '.join([str(i) for i in num_list]))
