import math
import unittest
import triangle


class TestTriangle(unittest.TestCase):
    def test_classify_ScaleneAndRight(self):
        self.assertEqual(triangle.classify(3, 4, 5), 'scalene')
        self.assertEqual(triangle.ifright(3, 4, 5), 'Right')

    def test_classify_ScaleneButNotRight(self):
        self.assertEqual(triangle.classify(3, 4, 6), 'scalene')
        self.assertEqual(triangle.ifright(3, 4, 6), 'Not Right')

    def test_classify_isosceles(self):
        self.assertEqual(triangle.classify(3, 3, 4), 'isosceles')
        self.assertEqual(triangle.ifright(3, 3, 4), 'Not Right')

    def test_classify_isoscelesAndRight(self):
        self.assertEqual(triangle.classify(2, 2, (2* (math.sqrt(2)))), 'isosceles')
        self.assertEqual(triangle.ifright(2, 2, (2* (math.sqrt(2)))), 'Right')

    def test_classify_Equilateral(self):
        self.assertEqual(triangle.classify(3, 3, 3), 'Equilateral')
        self.assertEqual(triangle.ifright(3, 3, 3), 'Not Right')
        # Equilateral Triangles are impossible to be right triangles #



    def test_classify_invalid(self):
        self.assertEqual(triangle.classify(1, 2, 5), 'invalid')


if __name__ == "__main__":
    unittest.main()
