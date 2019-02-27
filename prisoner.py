brick1, brick2, brick3 = int(input()), int(input()), int(input())
hole1, hole2 = int(input()), int(input())
if hole1 >= brick1:
    if hole2 >= brick2 or hole2 >= brick3:
        print('Yes')
    else:
        print('No')
elif hole1 >= brick2:
    if hole2 >= brick1 or hole2 >= brick3:
        print('Yes')
    else:
        print('No')
elif hole1 >= brick3:
    if hole2 >= brick1 or hole2 >= brick2:
        print('Yes')
    else:
        print('No')
else:
    print('No')
