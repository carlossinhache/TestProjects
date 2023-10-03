def count(param):
    syll_count = 1
    for char in param:
        if char == "-":
            syll_count += 1
    return syll_count


print(count("met-a-phor"))