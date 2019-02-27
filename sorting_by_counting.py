A = list(map(int, input().split()))


def CountSort(A):
    t = [0] * 101
    for i in A:
        t[i] += 1
    A = []
    for i in range(101):
        A += [i] * t[i]
    print(*A)


CountSort(A)
