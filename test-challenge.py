def only_ints(parm1, parm2):
    if isinstance(parm1, int) and isinstance(parm2, int):
        return True
    return False


print(only_ints(2, "test"))