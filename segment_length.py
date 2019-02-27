from math import sqrt


def distance(x1, y1, x2, y2):
    length = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
    print('{0:.5f}'.format(length))


distance(float(input()), float(input()), float(input()), float(input()))
