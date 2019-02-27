def adding():
    num = int(input())
    if num == 0:
        return 0
    return num + adding()


print(adding())
