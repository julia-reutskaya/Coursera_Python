km1 = int(input())
km2 = int(input())
i = 1
while km1 < km2:
    km3 = km1 * 0.1
    km1 = km1 + km3
    i = i + 1
print(i)
