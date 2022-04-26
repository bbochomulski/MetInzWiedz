import numpy as np


A = np.array([
    [2, 4, 1, 6],
    [8, 1, 2, 3],
    [1, 2, 1, 5],
    [3, 1, 2, 7],
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
        list_of_e_vectors.append(u_vector/(np.sum(u_vector**2)**0.5))

    Q = np.array(list_of_e_vectors).T[0]
    R = np.dot(Q.T, matrix)

    return Q, R


def matrix_eigenvalues(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        return "Matrix is not square"
    print("Expected outcome: \n", np.linalg.eigvals(matrix))
    matrix = matrix.copy()
    eigenvalues = np.diag(matrix)
    eigenvalues_new = np.ones(matrix.shape[0])
    i = 0
    while not np.allclose(eigenvalues, eigenvalues_new, 0.000000001):
        eigenvalues = eigenvalues_new
        Q, R = qr_matrix(matrix)
        matrix = np.dot(R, Q)
        eigenvalues_new = np.diag(matrix)
        i += 1
    print("Iterations: ", i)
    return eigenvalues_new


print("Outcome: \n", matrix_eigenvalues(A))
