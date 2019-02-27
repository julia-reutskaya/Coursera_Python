num_list = list(map(int, input().split()))
num_set = set()
for num in num_list:
    if num in num_set:
        print('YES')
    else:
        print('NO')
        num_set.add(num)
