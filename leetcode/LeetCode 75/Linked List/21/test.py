import unittest
import solution as s
from .. import linked_list_test_util as util

class TestInteraction(unittest.TestCase) :
    def _traversal(self, ll1, ll2, resultArray) :
        a = util.array_to_linked_list(ll1)
        b = util.array_to_linked_list(ll2)
        c = s.Solution().mergeTwoLists(a, b)
        self.assertListEqual(util.linked_list_to_array(c), resultArray)

    def test_two_empty_lists(self):
        self._traversal([], [], [])

    def test_one_empty_list(self):
        self._traversal([], [0], [0])

    def test_two_lists_starting_with_same_value(self):
        self._traversal([1,2,4], [1,3,4], [1,1,2,3,4,4])
    
    