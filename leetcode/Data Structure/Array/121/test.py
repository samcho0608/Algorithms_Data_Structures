import unittest
import solution as s

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

class TestInteraction(unittest.TestCase) :

    def test_decreasingOrder(self) :
        self.assertEqual(s.Solution().maxProfit([7,6,4,3,1]), 0)
    
    def test_increasingOrder(self) :
        self.assertEqual(s.Solution().maxProfit([1,2,4,6,7]), 6)

    def test_length_one(self) :
        self.assertEqual(s.Solution().maxProfit([0]), 0)
    
    def test_increasing_then_decreasing1(self) :
        self.assertEqual(s.Solution().maxProfit([1,2,1]), 1)
    
    def test_increasing_then_decreasing2(self) :
        self.assertEqual(s.Solution().maxProfit([1,2,3,1]), 2)

    def test_increasing_then_decreasing3(self) :
        self.assertEqual(s.Solution().maxProfit([1,2,3,2,1]), 2)
    # def test_no_order(self) :
    #     self.assertEqual(s.Solution().maxProfit([7,1,5,3,6,4]), 5)