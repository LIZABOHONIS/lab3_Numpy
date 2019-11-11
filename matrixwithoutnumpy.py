from itertools import starmap
from operator import mul
import random
# starmap(function,iterable)- застосовує ф-цію до кожного елемента послідовності
# mul - множення

class My_Matrix:
    
    def create_random_matrix(self, rows, columns):
        random.seed(3)
        matr = [[random.random()
                 for i in range(columns)]
                for j in range(rows)]
        return matr

    def create_vector(self, element):
        random.seed(1)
        return [random.random() for i in range(element)]

    def multy_two_matrix(self, a, b):
        c = [[0 for row in range(len(b[0]))] for col in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    c[i][j] += a[i][k] * b[k][j]
        return c

    def multy_vector_on_vector(self, vector1, vector2):
        return [vector1[i] * vector2[i] for i in range(len(vector1))]

    def multy_vector_matrix(self, vector, matrix):
        return [sum(starmap(mul, zip(vector, col))) for col in zip(*matrix)]
    
if __name__ == '__main__':
    A = My_Matrix()

    m1 = A.create_random_matrix(20,5)
    m2 = A.create_random_matrix(5,20)
    print("Matrix A:", m1)
    print("Matrix B:", m2)

    v1 = A.create_vector(20)
    v2 = A.create_vector(20)
    print("Vector V1:", v1)
    print("Vector V2:", v2)

    c1 = A.multy_two_matrix(m1,m2) #множення матриць
    print("Multy two matrix:",c1)

    k1 = A.multy_vector_on_vector(v1,v2) #множення векторів
    print("Multy vector on vector:",k1)

    f1 = A.multy_vector_matrix(v1,m1)  #множення вектора на матрицю
    print("Multy vector on matrix:",f1)
    
import time

start_time = time.clock()
print ("program execution time: ", time.clock() - start_time, "seconds")




    
    
