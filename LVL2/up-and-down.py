def trash_up_down(num):
    lower_than_num = num
    higher_than_num = num

    while lower_than_num >= num:
        lower_than_num = lower_than_num - 1
    while higher_than_num <= num:
        higher_than_num = higher_than_num + 1
    return (lower_than_num, higher_than_num)


def up_down(num):
    return (num - 1, num + 1)


print(up_down(5))
