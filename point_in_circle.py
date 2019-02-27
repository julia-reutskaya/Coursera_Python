def IsPointInCircle(x, y, xc, yc, r):
    return (xc - x)**2 + (yc - y)**2 <= r**2


def point_coordinate(x, y, xc, yc, r):
    if IsPointInCircle(x, y, xc, yc, r):
        print('Yes')
    else:
        print('No')


point_coordinate(float(input()), float(input()), float(input()),
                 float(input()), float(input()))
