num = int(input())
largestNum = num
i = 1
while num != 0:
    num = int(input())
    if num >= largestNum:
        if num == largestNum:
            i += 1
        elif num > largestNum:
            i = 1
        largestNum = num
print(i)
