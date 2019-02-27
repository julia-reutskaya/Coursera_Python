in_data = open("input.txt", "r", encoding="utf8")
out = open('output.txt', 'w', encoding='utf8')
k = int(in_data.readline())
my_list = []
for line in in_data:
    new_line = line.split()
    if int(new_line[-1]) >= 40 and int(new_line[-2]) >= 40 \
            and int(new_line[-3]) >= 40:
        my_list.append(new_line)
in_data.close()
my_list.sort(key=lambda a: int(a[-1]) + int(a[-2]) + int(a[-3]))
my_list.reverse()
competition = []
for i in my_list:
    score_sum = int(i[-1]) + int(i[-2]) + int(i[-3])
    competition.append(score_sum)
n = len(competition)


def score_competition(n, k, competition):
    if n <= k:
        return 0
    elif competition[k] == competition[0]:
        return 1
    for i in range(k, 0, -1):
        if competition[i] < competition[i - 1]:
            return competition[i - 1]


print(score_competition(n, k, competition), file=out)
