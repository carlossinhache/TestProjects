def capital_indexes(param):
    lst = []
    inx = -1
    for letter in param:
        inx += 1
        if letter.isupper():
            lst.append(inx)
    return lst


param = "heLLo"
print((capital_indexes(param)))
