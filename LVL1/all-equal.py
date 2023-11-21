def all_equal(my_list):
    if not my_list:
        return True

    first_element = my_list[0]
    return all(element == first_element for element in my_list)


print(all_equal([1, 1, 2]))
