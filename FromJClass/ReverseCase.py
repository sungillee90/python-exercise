
def reverse(str):
    # Base Case
    if len(str) < 2:
        return str
    # Recursive case
    else:
        return reverse(str[1:]) + str[0]

print(reverse("Sung Il"))