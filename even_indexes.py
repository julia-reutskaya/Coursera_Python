num_list = list(map(int, input().split()))
even_index = num_list[::2]
print(' '.join(map(str, even_index)))
