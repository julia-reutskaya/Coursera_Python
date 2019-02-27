a, b, c = int(input()), int(input()), int(input())
if a > c:
    (a, c) = (c, a)
    if b <= a:
        (b, a) = (a, b)
    elif b >= c:
        (b, c) = (c, b)
elif b > c:
    (b, c) = (c, b)
    if c <= a:
        (c, a) = (a, c)
elif a > b:
    (a, b) = (b, a)
    if b >= c:
        (b, c) = (c, b)
print(a, b, c)
