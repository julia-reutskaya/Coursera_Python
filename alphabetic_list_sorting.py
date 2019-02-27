in_data = open('input.txt', 'r', encoding='utf8')
out = open('output.txt', 'w', encoding='utf8')
data = in_data.read().split()
k = 0
result = {}
for i in data:
    if k % 4 == 0:
        result[data[k]] = (data[k + 1], data[k + 3])
    k += 1
for j in sorted(result.keys()):
    print(' '.join(map(str, (j, ' '.join(map(str, result[j]))))), file=out)
