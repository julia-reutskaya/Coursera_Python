overal_space_user = list(map(int, input().split()))
list_spaces = []


def input_user_space(count):
    for i in range(count):
        user_space = int(input())
        list_spaces.append(user_space)
    return list_spaces


def fit_in_overal_space(overal_space, list_user_spaces):
    list_user_spaces.sort()
    fit_in = sum(list_user_spaces)
    if fit_in <= overal_space:
        print(len(list_user_spaces))
    else:
        list_user_spaces.pop(len(list_user_spaces) - 1)
        fit_in_overal_space(overal_space, list_user_spaces)


each_user_space = input_user_space(overal_space_user[1])
fit_in_overal_space(overal_space_user[0], each_user_space)
