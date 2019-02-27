village_count = int(input())
village_distance = map(int, input().split())
shelter_count = int(input())
shelter_distance = list(map(int, input().split()))

for i in range(len(shelter_distance)):
    shelter_distance[i] = [i + 1, shelter_distance[i]]

shelter_distance.sort(key=lambda x: x[1])


def find_value(village):
    if village < shelter_distance[0][1]:
        return shelter_distance[0][0]
    if village > shelter_distance[-1][1]:
        return shelter_distance[-1][0]
    j = 0
    k = len(shelter_distance) - 1
    while k - j > 1:
        m = (k + j) >> 1
        if shelter_distance[m][1] < village:
            j = m
        else:
            k = m
    if village - shelter_distance[j][1] < shelter_distance[k][1] - village:
        return shelter_distance[j][0]
    else:
        return shelter_distance[k][0]


print(*[find_value(v) for v in village_distance])
