cow = int(input())
if 10 <= cow <= 20:
    print(cow, 'korov')
elif cow % 10 == 1:
    print(cow, 'korova')
elif (cow % 10 == 0) or (cow % 10 != 2 and cow % 10 != 3 and cow % 10 != 4):
    print(cow, 'korov')
else:
    print(cow, 'korovy')
