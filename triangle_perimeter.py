from math import sqrt


def distance(x1, y1, x2, y2, x3, y3):
    side_a = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    side_b = sqrt(pow(x2 - x3, 2) + pow(y2 - y3, 2))
    side_c = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2))
    perimeter(side_a, side_b, side_c)


def perimeter(a, b, c):
    res = a + b + c
    print('{0:.6f}'.format(res))


distance(float(input()), float(input()), float(input()),
         float(input()), float(input()), float(input()))

