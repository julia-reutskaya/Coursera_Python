num1 = int(input())
num2 = int(input())
if num1 <= num2:
    for i in range(num1, num2 + 1):
        print(i, end=' ')
elif num1 >= num2:
    for i in range(num1, num2 - 1, -1):
        print(i, end=' ')
