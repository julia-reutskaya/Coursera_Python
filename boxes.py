boxA1, boxA2, boxA3 = int(input()), int(input()), int(input())
boxB1, boxB2, boxB3 = int(input()), int(input()), int(input())
if boxA1 > boxA3:
    (boxA1, boxA3) = (boxA3, boxA1)
    if boxA2 <= boxA1:
        (boxA2, boxA1) = (boxA1, boxA2)
    elif boxA2 >= boxA3:
        (boxA2, boxA3) = (boxA3, boxA2)
elif boxA2 > boxA3:
    (boxA2, boxA3) = (boxA3, boxA2)
    if boxA3 <= boxA1:
        (boxA3, boxA1) = (boxA1, boxA3)
elif boxA1 > boxA2:
    (boxA1, boxA2) = (boxA2, boxA1)
    if boxA2 >= boxA3:
        (boxA2, boxA3) = (boxA3, boxA2)
if boxB1 > boxB3:
    (boxB1, boxB3) = (boxB3, boxB1)
    if boxB2 <= boxB1:
        (boxB2, boxB1) = (boxB1, boxB2)
    elif boxB2 >= boxB3:
        (boxB2, boxB3) = (boxB3, boxB2)
elif boxB2 > boxB3:
    (boxB2, boxB3) = (boxB3, boxB2)
    if boxB3 <= boxB1:
        (boxB3, boxB1) = (boxB1, boxB3)
elif boxB1 > boxB2:
    (boxB1, boxB2) = (boxB2, boxB1)
    if boxB2 >= boxB3:
        (boxB2, boxB3) = (boxB3, boxB2)
if boxA1 == boxB1 and boxA2 == boxB2 and boxA3 == boxB3:
    print('Boxes are equal')
elif boxA1 >= boxB1 and boxA2 >= boxB2 and boxA3 >= boxB3:
    print('The first box is larger than the second one')
elif boxA1 <= boxB1 and boxA2 <= boxB2 and boxA3 <= boxB3:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
