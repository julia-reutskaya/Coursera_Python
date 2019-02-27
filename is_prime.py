from math import sqrt


def IsPrime(n):
    i = 2
    while n % i != 0:
        if i >= sqrt(n):
            print('Yes')
            return
        i += 1
    if n == 2:
        print('Yes')
    else:
        print('No')


IsPrime(int(input()))
