import unittest
import unittestmy as my
import numpy as np


class MyTest(unittest.TestCase):

    def test_multy_2_vectors_2(self):
        print("id: " + self.id())
        self.assertEqual(my.multy_2_vectors(np.array([3, 1, 3]),
                                             np.array([2, 4])), None)

    def test_multy_2_vectors_3(self):
        print("id: " + self.id())
        self.assertEqual(my.multy_2_vectors([3, 1, 3], [2, 2, 4]), None)

    def test_multy_2_matrix_1(self):
        print("id: " + self.id())
        self.assertEqual(my.multy_2_matrix(np.array([[2,3,4],[3,4,1]]),
                                            np.array([[2,1],[3,0],[4,2]])),
                                            [[29,10],[22,5]])

    def test_multy_2_matrix_2(self):
        print("id: " + self.id())
        self.assertEqual(my.multy_2_matrix(np.array([[2,3], [0,3]]),
                                            np.array([[0,9,3], [4,1,5], [5,1,4]])), None)

    def test_multy_vect_matr_1(self):
        print("id: " + self.id())
        self.assertEqual(my.multy_vect_matr(np.array([2,3,4,5]),
                                             np.array([[2,0,1], [3,0,1,], [3,1,2], [4,6,0,1]])),
                         ([45, 34, 13]))

    def test_multy_vector_matr_2(self):
        print("id: " + self.id())
        self.assertEqual(my.multy_vect_matr(np.array([2, 0]),
                                             np.array([2, 1, 3])), None)


if __name__ == '__main__':
    unittest.main()
