def func_R(n):
    print("Start: " + str(n))
    res = 0
    if n == 0:
        res = 0
    else:
        res = func_R(n-1)+1
    print("End: " + str(n))
    return res


print(func_R(0))
print(func_R(3))