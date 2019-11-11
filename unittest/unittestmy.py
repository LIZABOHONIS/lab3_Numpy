import numpy as np
from itertools import starmap
from operator import mul


def generate_data(n):
    np.random.seed(0)
    a = np.random.rand(n)
    b = np.random.rand(n)
    return a, b


def generate_matrix(n, m):
    np.random.seed(0)
    a = np.random.rand(n, m)
    b = np.random.rand(n, m)
    return a, b


def multy_2_vectors(v1, v2):
    if (not isinstance(v1, np.ndarray)) or (not isinstance(v2, np.ndarray)):
        return None
    if len(v1) != len(v2):
        return None
    v3 = 0.0
    for i in range(len(v1)):
        v3 += v1[i] * v2[i]
    return v3


def multy_2_matrix(m1, m2):
    if (not isinstance(m1, np.ndarray)) or (not isinstance(m2, np.ndarray)):
        return None
    if len(m1[0]) != len(m2):
        return None
    c = [[0 for row in range(len(m2[0]))] for col in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m1[0])):
                c[i][j] += m1[i][k] * m2[k][j]
    return c


def multy_vect_matr(v, m):
    if (not isinstance(v, np.ndarray)) or (not isinstance(m, np.ndarray)):
        return None
    if np.all(len(v) != len(m)):
        return None
    return [sum(starmap(mul, zip(v, col))) for col in zip(*m)]


def multy_2_vectors_numpy(v1, v2):
    if (not isinstance(v1, np.ndarray)) or (not isinstance(v2, np.ndarray)):
        return None
    if len(v1) != len(v2):
        return None
    return np.dot(v1, v2)


def multy_2_matrix_numpy(m1, m2):
    if (not isinstance(m1, np.ndarray)) or (not isinstance(m2, np.ndarray)):
        return None
    if len(m1[0]) != len(m2):
        return None
    return np.dot(m1, m2)


def multy_vect_matr_numpy(v, m):
    if (not isinstance(v, np.ndarray)) or (not isinstance(m, np.ndarray)):
        return None
    if len(v) != len(m):
        return None
    return np.dot(v, m)
