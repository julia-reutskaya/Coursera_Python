percent = int(input())
doll = int(input())
cents = int(input())
years = int(input())
percentAfterYear = 0
i = 1
totalCents = doll * 100 + cents
while i <= years:
    percentAfterYear = totalCents + (totalCents * percent / 100)
    doll = int(percentAfterYear // 100)
    cents = int(percentAfterYear % 100)
    totalCents = doll * 100 + cents
    i += 1
print(doll, cents)
