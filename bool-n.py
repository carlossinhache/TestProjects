def triple_and(param1, param2, param3):
    if param1 is True and param2 is True and param3 is True:
        return True
    return False


def triple_and2(a, b, c):
    return a and b and c


print(triple_and2(True, True, True))
