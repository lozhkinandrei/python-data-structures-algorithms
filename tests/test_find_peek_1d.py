import unittest
from problems.find_peak_1d import find_peak_1d_while_loop, find_peak_1d_recursive


class TestFindPeek1D(unittest.TestCase):
    def setUp(self):
        self.array1 = [0]
        self.array2 = [1,2,3,4,5,6,7,8,9,10]
        self.array3 = [1,6,4,7,2,1,4,7]
        self.array4 = [10,2,3,4,5,7,8]
        self.array5 = [1,1,1,1,1,3]
        self.array6 = [1,7,9,20,3]

    def test_while_loop_implementation(self):
        self.assertEqual(0, find_peak_1d_while_loop(self.array1))
        self.assertEqual(10, find_peak_1d_while_loop(self.array2))
        self.assertEqual(6, find_peak_1d_while_loop(self.array3))
        self.assertEqual(8, find_peak_1d_while_loop(self.array4))
        self.assertEqual(1, find_peak_1d_while_loop(self.array5))
        self.assertEqual(20, find_peak_1d_while_loop(self.array6))

    def test_recursive_implementation(self):
        self.assertEqual(0, find_peak_1d_recursive(self.array1))
        self.assertEqual(10, find_peak_1d_recursive(self.array2))
        self.assertEqual(6, find_peak_1d_recursive(self.array3))
        self.assertEqual(8, find_peak_1d_recursive(self.array4))
        self.assertEqual(1, find_peak_1d_recursive(self.array5))
        self.assertEqual(20, find_peak_1d_recursive(self.array6))


if __name__ == '__main__':
    unittest.main()
