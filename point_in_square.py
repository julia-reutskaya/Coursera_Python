def IsPointInSquare(x, y):
    return (-1 <= x <= 1) and (-1 <= y <= 1)


def point_coordinate(a, b):
    if IsPointInSquare(a, b):
        print('Yes')
    else:
        print('No')


point_coordinate(float(input()), float(input()))
