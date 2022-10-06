import unittest
import solution as s

class TestIntersect(unittest.TestCase) :

    def test_intersection_two_repeated_numbers(self) :
        self.assertEqual(s.Solution().intersect([1,2,2,1],[2,2]), [2,2])
    
    def test_intersection_one_element_shown_twice_in_other(self):
        # self.assertEqual(s.Solution().intersect([4,9,5], [9,4,9,8,4]), [4,9])
        self.assertListEqual(s.Solution().intersect([4,9,5], [9,4,9,8,4]), [9,4])