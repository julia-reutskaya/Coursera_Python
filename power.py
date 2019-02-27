a = float(input())
n = int(input())


def power(b, c):
    if b == 0:
        return 0
    elif c == 0:
        return 1
    else:
        return b * power(b, c - 1)


print(power(a, n))
