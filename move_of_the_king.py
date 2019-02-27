kPos1 = int(input())
kPos2 = int(input())
mPos1 = int(input())
mPos2 = int(input())
if (kPos1 + 1 == mPos1 or kPos1 - 1 == mPos1 or kPos1 == mPos1) \
        and (kPos2 + 1 == mPos2 or kPos2 - 1 == mPos2 or kPos2 == mPos2):
    print('Yes')
else:
    print('No')
