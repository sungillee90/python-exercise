def nested_loop():
    for i in [1, 2, 3]:
        for j in [4, 5, 6]:
            print(str(i) + str(j))

nested_loop()

def print_pyramid(n):
    for i in range(n):
        line_to_print = ""
        for j in range(i):
            line_to_print += "o"
        print(line_to_print)
    return

print_pyramid(5)