a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
delta = a * d - b * c
deltaX = d * e - b * f
deltaY = a * f - c * e
x = deltaX / delta
y = deltaY / delta
print(x, y)
