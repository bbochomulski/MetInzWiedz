import numpy as np

A = np.array([
    [2, 4, 1, 6],
    [8, 1, 2, 3],
    [1, 2, 1, 5],
    [3, 1, 2, 7]
])
A = np.array([
    [2, 2, 1],
    [6, 4, 0],
    [2, 2, 2]
])


def qr_matrix(matrix):
    list_of_vectors = []
    for i in range(matrix.shape[1]):
        vector = np.array([[matrix[j][i]] for j in range(matrix.shape[0])])
        list_of_vectors.append(vector)

    list_of_u_vectors = []
    list_of_e_vectors = []

    for vector in list_of_vectors:
        projections_sum = 0
        for u_vector in list_of_u_vectors:
            projections_sum += (np.dot(u_vector.T, vector)/np.dot(u_vector.T, u_vector))*u_vector
        u_vector = vector - projections_sum
        list_of_u_vectors.append(u_vector)
        e_vector = u_vector/(np.sum(u_vector**2)**0.5)
        list_of_e_vectors.append(e_vector)

    Q = np.array(list_of_e_vectors).T[0]
    R = np.dot(Q.T, matrix)

    return Q, R


def matrix_eigenvalues(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return "Matrix is not square"
    matrix = matrix.copy()
    eigenvalues = np.diag(matrix)
    eigenvalues_new = np.ones(matrix.shape[0])
    while not np.allclose(eigenvalues, eigenvalues_new, 1e-10):
        eigenvalues = eigenvalues_new
        Q, R = qr_matrix(matrix)
        matrix = np.dot(R, Q)
        eigenvalues_new = np.diag(matrix)
    return eigenvalues_new


def gauss_jordan(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return "Matrix is not square"
    matrix = matrix.copy()
    n = matrix.shape[0]
    epsilon = 1e-5
    eigenvector = matrix_eigenvalues(matrix).tolist()
    for i in range(n-1):
        for j in range(i+1, n):
            if np.abs(matrix[i][j]) < epsilon:
                raise ZeroDivisionError
            m = matrix[j][i] / matrix[i][i]
            for k in range(i+1, n):
                matrix[j][k] += m * matrix[i][k]

    for i in range(n-1, -1, -1):
        s = matrix[i][n-1]
        for j in range(i, n, -1):
            s -= matrix[i][j] * eigenvector[j]
            if np.abs(matrix[i][i]) < epsilon:
                raise ZeroDivisionError
        eigenvector[i] = s / matrix[i][i]

    return eigenvector


def matrix_eigenvectors(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return "Matrix is not square"
    matrix = matrix.copy()
    eigenvalues = matrix_eigenvalues(matrix)
    print(eigenvalues)
    eigenvectors = []
    for eigenvalue in eigenvalues:
        eigen_matrix = matrix - np.diag(np.ones(matrix.shape[0])*eigenvalue)
        eigenvectors.append(gauss_jordan(eigen_matrix))
    return eigenvectors


print(matrix_eigenvectors(A))
