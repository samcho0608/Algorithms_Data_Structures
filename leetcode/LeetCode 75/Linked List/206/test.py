import unittest
import solution as s
from .. import linked_list_test_util as util

class TestInteraction(unittest.TestCase) :
    def _traversal(self, ll, resultArray) :
        a = util.array_to_linked_list(ll)
        b = s.Solution().reverseList(a)
        self.assertListEqual(util.linked_list_to_array(b), resultArray)
    def test_reverse_1(self):
        self._traversal([1,2,3,4,5], [5,4,3,2,1])
    def test_reverse_2(self):
        self._traversal([1,2], [2,1])
    def test_reverse_3(self):
        self._traversal([], [])