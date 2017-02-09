# test loop and comprehension implementations

from comprehension import dot_prod, matrix_vector_prod
from comprehension import  pythagorean_triples, any_pythagorean_triples
# uncomment these to test your implementations
# from loop import dot_prod
# from loop import matrix_vector_prod
# from loop import pythagorean_triples
# from loop import any_pythagorean_triples

import unittest

class DotProductTester(unittest.TestCase):

    def setUp(self: unittest.TestCase) -> None:
        self._zero_vector = [0.0, 0.0, 0.0]

    def tearDown(self: unittest.TestCase) -> None:
        self._zero_vector = None

    def test_zero_case(self: unittest.TestCase) -> bool:
        """Dot product of zero vectors is zero?"""
        self.assertEqual(dot_prod(self._zero_vector, self._zero_vector), 0.0)


class MatrixVectorProductTester(unittest.TestCase):

    def setUp(self: unittest.TestCase) -> None:
        self._identity_matrix = [[1, 0], [0, 1]]
        self._zero_vector = [0.0, 0.0]

    def tearDown(self: unittest.TestCase) -> None:
        self._identity_matrix = None
        self._zero_vector = None

    def test_zero_case(self: unittest.TestCase) -> bool:
        """Identity times zero matrix is zero"""
        self.assertEqual(matrix_vector_prod(self._identity_matrix, 
                                            self._zero_vector), 
                         self._zero_vector)



class PythagoreanTripleTester(unittest.TestCase):

    def test_10(self: unittest.TestCase) -> None:
        """triples up to 10"""
        self.assertEqual(set(pythagorean_triples(10)), {(3, 4, 5), (6, 8, 10)})


class AnyPythagoreanTripleTester(unittest.TestCase):

    def test_100_110(self: 'AnyPythagoreanTripleTester') -> bool:
        """triples in [100, 110]?"""
        self.assertFalse(any_pythagorean_triples(100, 110))
        
if __name__ == '__main__':
    unittest.main(exit=False)
