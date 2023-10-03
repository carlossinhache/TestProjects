def only_ints(parm1, parm2):
    if type(parm1) is int and type(parm2) is int:
        return True
    return False


print(only_ints(2, True))