import numpy as np
import random

#множення двох матриць
A = np.random.rand(20,5) #N=200
B = np.random.rand(5,20) #N=200
C = np.random.rand(5)
C1 = np.random.rand(5)
K = np.dot(A,B) #множення матриць
L = np.dot(A,C) #множення матриці на вектор
L1 = np.dot(C,B) #множення вектора на матрицю
P = np.dot(C,C1) #множення вектора на вектор
print("Matrix A:", A)
print("Matrix B:", B)
print("Vector C:", C)
print("Vector C1:", C1)
print("Множення двох матриць:", K)
print("Множення матриці на вектор:", L)
print("Множення вектора на матрицю:", L1)
print("Множення вектора на вектор:", P)

import time


start_time = time.clock()
print ("program execution time: ", time.clock() - start_time, "seconds")