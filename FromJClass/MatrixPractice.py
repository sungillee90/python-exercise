# r1 = [1, 2, 3]
# r2 = [4, 5, 6]
# r3 = [7, 8, 9]
#
# matrix = [r1, r2, r3]
#
# matrix_two = [[1, 2, 3, 5],
#               [1, 2, 4, 6],
#               [4, 5, 8, 7]]
#
# print(matrix)
# print(matrix_two)
# #  matrix [Row][Column] [0] [1] [2]
# print(matrix_two[2][1])
#
# # print all of the single element
# def print_matrix(m):
#     if m == []:
#         return
#     num_rows = len(m)
#     num_cols = len(m[0])
#
#     for row in m:
#         for num in row:
#             print(num)
#
#     print(num_rows)
#     print(num_cols)
#
#
# print_matrix(matrix_two)

def creat_matrix(m,n):
    my_matrix = []
    for i in range(m):
        my_matrix.append([0,0,0,0])
    print(my_matrix)
    return my_matrix

creat_matrix(3,4)