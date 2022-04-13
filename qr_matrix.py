import numpy as np

A = np.array([[1, 0], [1, 1], [0, 1]])

v1 = np.array([[x[0]] for x in A])
v2 = np.array([[x[1]] for x in A])

u1 = np.array([[1], [1], [0]])
l1 = np.sqrt(np.dot(u1.T, u1))
e1 = u1 / l1

proj_u1_v2 = np.dot(v2.T, u1) / np.dot(u1.T, u1) * u1

u2 = v2 - proj_u1_v2

l2 = np.sqrt(np.dot(u2.T, u2))
e2 = u2 / l2

Q = np.array([[e1[0], e2[0]], [e1[1], e2[1]], [e1[2], e2[2]]])

R = Q.T @ A

new_A = np.round(np.array([x[0] + x[1] for x in (Q * R)]))
print(new_A)

