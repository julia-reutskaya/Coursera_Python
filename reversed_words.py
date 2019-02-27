s = str(input())
space = s.find(' ')
first = s[:space]
second = s[space + 1:]
print(second, first)
