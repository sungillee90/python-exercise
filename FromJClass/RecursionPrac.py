def func_R(n):
    if n == 0:
        return 0
    else:
        return func_R(n-1)+1


print(func_R(3))