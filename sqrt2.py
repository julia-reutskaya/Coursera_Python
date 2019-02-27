from math import sqrt
a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4 * a * c
if a == b == 0:
    print(3)
elif d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    if x1 > x2:
        print(2, x2, x1)
    elif x1 < x2:
        print(2, x1, x2)
elif d == 0:
    x = -b / (2 * a)
    print(1, x)
elif d < 0:
    print(0)
