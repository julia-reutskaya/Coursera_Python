num = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
num_list = num_list[:num]
print(*num_list)
