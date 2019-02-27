num_list = list(map(int, input().split()))
n = 0
for i in num_list:
    n = num_list[i]
    if i > 0:
        n += 1
print(n)
