def all_equal(my_list):
    inx = 0
    temp = True
    while temp:
        if my_list[0] == my_list[inx]:
            inx += 1
    return False


print(all_equal([]))
