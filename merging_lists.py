list_one = list(map(int, input().split()))
list_two = list(map(int, input().split()))


def merge(list_a, list_b):
    list_c = list_a + list_b
    j = 0
    while j <= len(list_c):
        for i in range(1, len(list_c)):
            if list_c[i] < list_c[i - 1]:
                list_c[i], list_c[i - 1] = list_c[i - 1], list_c[i]
        j += 1
    print(' '.join([str(i) for i in list_c]))


merge(list_one, list_two)
