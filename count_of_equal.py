num = int(input())
num1 = num
count = 1
largestCount = 1
while num != 0:
    num = int(input())
    if num == num1:
        count += 1
    elif largestCount <= count:
        largestCount = count
        count = 1
    elif num != num1:
        count = 1
    num1 = num
print(largestCount)
