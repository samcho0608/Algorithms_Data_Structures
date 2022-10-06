import unittest
import solution as s

class TestInteraction(unittest.TestCase) :
    def pascal_test(self, numRow, expected):
        res = s.Solution().generate(numRow)
        for i in range(numRow) :
            self.assertListEqual(res[i], expected[i])

    def test_row_length_1(self):
        self.pascal_test(1, [[1]])    

    def test_row_length_5(self):
        self.pascal_test(5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
        