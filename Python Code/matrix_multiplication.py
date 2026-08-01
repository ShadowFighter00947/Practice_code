# Initialize an empty matrix c to zero.
# I need to consider two matrix A and B.
# I need to find the dot product of two matrix.
# I need to find the ith and jth value of matrix.

def initialize_mat(dim):
    c = []
    for i in range(dim):
        c.append([])
    for i in range(dim):
        for j in range(dim):
            c[i].append(0)
    return c

def dot_product(u, v):
    dim = len(u)
    ans = 0
    for i in range(dim):
        ans = ans + (u[i] * v[i])
    return ans

def row(A, i):
    dim = len(A)
    l = []
    for k in range(dim):
        l.append(A[i][k])
    return l

def column(A, j):
    dim = len(A)
    l = []
    for k in range(dim):
        l.append(A[k][j])
    return l

def mat_multiple(A, B):
    dim = len(A)
    c = initialize_mat(dim)
    for i in range(dim):
        for j in range(dim):
            c[i][j] = dot_product(row(A, i), column(B, j))
    return c 

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[4,5,6],[7,8,9]]

print(mat_multiple(A, B))