def square_list(nums_list):
    i = 0
    while i < len(nums_list):
        nums_list[i] = nums_list[i] *nums_list[i]
        i += 1

    return nums_list

square_list([1, 2, 3, 4, 5])
print(square_list([1, 2, 3, 4, 5]))