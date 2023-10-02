def only_ints(parm1, parm2):
    if parm1 and parm2 is int:
        return True
    return False

print(only_ints(2, 1))