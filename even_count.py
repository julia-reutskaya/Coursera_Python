num = int(input())
count = 0
while num != 0:
    if num % 2 == 0:
        count += 1
    num = int(input())
print(count)
