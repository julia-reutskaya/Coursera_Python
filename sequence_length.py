num = int(input())
count = 1
if num == 0:
    print(0)
else:
    while num != 0:
        num = int(input())
        if num != 0:
            count += 1
    print(count)
