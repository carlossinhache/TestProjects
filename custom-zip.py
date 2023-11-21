def zap(a, b):
    result = []
    for i in range(len(a)):
        item_from_a = a[i]
        item_from_b = b[i]
        tup = (item_from_a, item_from_b)
        result.append(tup)
    return result


# # concise solution with list comprehensions
# def zap(a, b):
#     return [(a[i], b[i]) for i in range(len(a))]

print(zap([1, 3], [2, 4]))
