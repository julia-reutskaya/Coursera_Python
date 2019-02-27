from math import ceil, floor
n = float(input())
b = n - int(n)
if b < 0.5:
    print(floor(n))
elif b >= 0.5:
    print(ceil(n))
