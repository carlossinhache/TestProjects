def flatten(list):
    flattened_list = []
    for item in list:
        flattened_list += item
    return flattened_list


print(flatten([[1, 2], [2, 1], [3, 4, 5, 6, 7]]))
