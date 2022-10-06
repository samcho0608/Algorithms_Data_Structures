import unittest
import solution as s

class TestInteraction(unittest.TestCase) :
    def test_not_possible(self) :
        mat = [[1,2], [3,4]]
        self.assertEqual(s.Solution().matrixReshape(mat, 2,4), mat)
    def test_2x2_to_1x4(self) :
        mat = [[1,2], [3,4]]
        res = s.Solution().matrixReshape(mat, 1, 4)
        expected = [[1,2,3,4]]
        for r in range(1) :
            self.assertListEqual(res[r], expected[r])
    def test_2x4_to_4x1(self):
        mat = [[1,2],[3,4]]
        res = s.Solution().matrixReshape(mat, 4, 1)
        expected = [[1],[2],[3],[4]]
        for r in range(4) :
            self.assertListEqual(res[r], expected[r])
    def test_1x2_to_1x1(self):
        mat = [[1,2]]
        res = s.Solution().matrixReshape(mat, 1, 1)
        self.assertEqual(res, mat)