from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int ) -> bool:
        targetRow = -1
        for i, row in enumerate(matrix) :
            if row[0] <= target and row[-1] >= target :
                targetRow = i
                break
        if targetRow == -1 :
            return False
        
        return target in matrix[i]