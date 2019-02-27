doll = int(input())
cents = int(input())
how_many = int(input())
cents_to_doll = cents * how_many // 100
cents_rest = cents * how_many % 100
doll_sum = doll * how_many + cents_to_doll
print(doll_sum, cents_rest)
