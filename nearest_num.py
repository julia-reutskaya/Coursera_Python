length = int(input())
num_list = list(map(int, input().split()))
n = int(input())
diff_list = []
i = 0
while i in range(length):
    m = abs(num_list[i] - n)
    diff_list.append(m)
    i += 1
min_val = min(diff_list)
for j in num_list:
    if n == j:
        print(j)
        break
    elif n >= j:
        if n - min_val == j:
            print(j)
            break
    elif n < j:
        if n + min_val == j:
            print(j)
            break
