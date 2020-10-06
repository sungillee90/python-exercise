
def has_even_number(lst):
    has_even = False
    for num in lst:
        if num % 2 == 0:
            has_even = True
            break
    print(has_even)
    return has_even

has_even_number([1, 2, 3])