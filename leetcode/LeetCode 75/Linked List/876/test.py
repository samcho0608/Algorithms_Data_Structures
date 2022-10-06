import unittest
import solution as s
from .. import linked_list_test_util as util

class TestInteraction(unittest.TestCase) :
    def _traversal(self, ll1, array) :
        stk1 = []

        while ll1 :
            stk1.append(ll1.val)
            ll1 = ll1.next

        self.assertListEqual(stk1, array)

    def test_example_1(self) :
        self._traversal(s.Solution().middleNode(util.array_to_linked_list([1,2,3,4,5])), [3,4,5])