in_data = open('input.txt', 'r', encoding='utf8')
data = int(in_data.readline())
num_set = set(range(1, data + 1))
num = set()

for line in in_data:
    if "YES" in line:
        num_set &= num
    elif "NO" in line:
        num_set -= num
    elif "HELP" not in line:
        num = set(map(int, line.split()))

print(*sorted(num_set))
