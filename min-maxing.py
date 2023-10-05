def largest_difference(arr):
    largest = 0
    smallest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    for num in arr:
        if num < smallest:
            smallest = num
    larg_diff = largest - smallest
    return larg_diff


print(largest_difference([33, 2, 100]))
