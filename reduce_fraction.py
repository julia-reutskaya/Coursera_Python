n = int(input())
m = int(input())


def ReduceFraction(n, m):
    def gcd(n, m):
        if n != 0 and m != 0:
            if n > m:
                n = n % m
            else:
                m = m % n
            return gcd(n, m)
        else:
            return n + m
    print((n // gcd(n, m)), (m // gcd(n, m)))


ReduceFraction(n, m)
