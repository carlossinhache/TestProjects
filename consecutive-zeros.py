def consecutive_zeros(str):
    max_zeros = 0
    zero_count = 0
    for num in str:
        if num == "0":
            zero_count += 1
        else:
            zero_count = 0
        max_zeros = max(max_zeros, zero_count)
    return max_zeros


print(consecutive_zeros("1001101000110"))
