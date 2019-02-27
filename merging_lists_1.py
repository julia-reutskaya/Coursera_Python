list_one = list(map(int, input().split()))
list_two = list(map(int, input().split()))


def merge(list_a, list_b):
    i = 0
    j = 0
    list_c = []
    while i < len(list_a) and j < len(list_b):
        if list_a[i] <= list_b[j]:
            list_c.append(list_a[i])
            i += 1
        else:
            list_c.append(list_b[j])
            j += 1
    while i < len(list_a):
        list_c.append(list_a[i])
        i += 1
    while j < len(list_b):
        list_c.append(list_b[j])
        j += 1
    print(*list_c)


merge(list_one, list_two)
