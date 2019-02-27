a = float(input())
b = int(input())


def power(a, b):
    if 0 == a:
        return 0
    if 0 == b:
        return 1
    if b % 2 == 0:
        return power(a, b / 2) ** 2
    return a * power(a, b - 1)


print(power(a, b))
