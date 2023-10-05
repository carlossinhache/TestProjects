def get_row_col(str):
    my_dict = {
        "A": 0,
        "B": 1,
        "C": 2
    }
    row = int(str[1]) -1
    column = my_dict[str[0]]
    str_tuple = (row, column)
    return str_tuple

print(get_row_col("B1"))
