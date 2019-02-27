s = str(input())
first = s.find('f')
index = s[first:].find('f', 1)
if first == -1:
    print(-2)
elif first != -1:
    index = s[first:].find('f', 1)
    if index == -1:
        print(-1)
    else:
        print(index + first)
