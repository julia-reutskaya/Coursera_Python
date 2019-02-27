n = int(input())
i = 1
series_sum = 0
while i <= n:
    calculation = 1/i**2
    series_sum += calculation
    i += 1
print('{0:.6f}'.format(series_sum))
