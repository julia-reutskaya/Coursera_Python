s = str(input())
first = s.find('f')
last = s.rfind('f')
if first == last == -1:
    pass
elif first != last:
    print(first, last)
elif first == last:
    print(first)
