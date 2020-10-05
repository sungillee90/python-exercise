def sum_list(num_list):
    total = 0
    i = 0
    while i < len(num_list):
        total += num_list[i]
        i += 1

    print(total)

sum_list([1, 2, 3, 4])