fnum_list = set(map(int, input().split()))
snum_list = set(map(int, input().split()))
print(*sorted(list(fnum_list & snum_list)))
