s = str(input())
deleteSymb = s.replace('@', '')
if s.count('@') == len(s):
    pass
else:
    print(deleteSymb)
