# Create a 0 matrix of size m x n where m is the num of rows and n is the num of colms

def create_matrix(m,n):
    my_matrix = []
    for i in range(m):
        my_row = []
        for j in range(n):
            my_row.append(0)
        my_matrix.append(my_row)
    return my_matrix

create_matrix(3,4)


# Add 2 marix m1 and m2 and return the resulting matrix
def add_matrices(m1, m2):
    if m1 == [] or m2 == []:
        return []
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return []
    num_rows = len(m1)
    num_cols = len(m1[0])

    m0 = create_matrix(num_rows, num_cols)
    for i in range(num_rows):
        for j in range(num_cols):
            m0[i][j] = m1[i][j] + m2[i][j]

    return m0

