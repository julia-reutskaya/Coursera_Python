a, b, c = int(input()), int(input()), int(input())
if (a == b) and (b == c):
    print(3)
elif (a == b or a == c or b == c) and (a != b or a != c or b != c):
    print(2)
else:
    print(0)