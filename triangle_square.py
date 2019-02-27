sideA = float(input())
sideB = float(input())
sideC = float(input())
p = (sideA + sideB + sideC) / 2
square = ((p * (p - sideA) * (p - sideB) * (p - sideC)) ** 0.5)
print('{0:.6f}'.format(square))
