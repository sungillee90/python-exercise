# def list_number():
#     lucky_numbers = [1,3,5,7,9,10]
#
#     print(lucky_numbers)
#     print(lucky_numbers[1]) #3
#     print(lucky_numbers[-1]) #10
#     print(lucky_numbers[-3]) #7
#     print(type(lucky_numbers))
#     print(lucky_numbers.append(15))
#     print(lucky_numbers)
#     print(lucky_numbers.pop(6))
#     print(lucky_numbers)
#
# list_number()

# P1: Write a fuction that prints each element in the list on a seperate line
def print_list(lst):
    i = 0
    while i < len(lst):
        print(lst[i])
        i += 1
    return
"""
print_list([1,2,3])
1
2
3
"""
print_list([1,2,4,5,6165])

#P2: Write a function outputs a list of numbers from 0 to n
