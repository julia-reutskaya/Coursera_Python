num = int(input())
firstLargest = num
secondLargest = 0
while num != 0:
    num = int(input())
    if num >= firstLargest:
        (secondLargest, firstLargest) = (firstLargest, num)
    elif (num >= secondLargest) and (num <= firstLargest):
        secondLargest = num
print(secondLargest)
