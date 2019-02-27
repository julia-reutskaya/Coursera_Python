s = str(input())
wordsCount = s.count(' ')
if s.rfind(' ') != (len(s) - 1):
    print(wordsCount + 1)
else:
    print(wordsCount)
