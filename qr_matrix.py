import numpy as np


A = np.array([
    [1, 0],
    [1, 1],
    [0, 1],
])


def qr_matrix(matrix):
    """
    Return the QR decomposition of a matrix
    """
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

    print(list_of_e_vectors)
    Q = np.array(list_of_e_vectors).T[0]
    R = np.dot(Q.T, matrix)

    return Q, R


Q, R = qr_matrix(A)

print(f"A:\n{A}")
print(f"Q:\n{Q}")
print(f"R:\n{R}")
print(f"QR:\n{np.round(np.dot(Q, R))}")
