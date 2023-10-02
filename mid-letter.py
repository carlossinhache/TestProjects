import math
def mid(string):
    str_len = len(string)
    if str_len % 2 == 0:
        return ""
    mid_char = string[math.floor(str_len/2)]
    return mid_char


print(mid("abc"))
