class Solution :
    def matrixReshape(self, mat, r, c):
        if len(mat) * len(mat[0]) != r * c :
            return mat
        res = [[None for _ in range(c)] for _ in range(r) ]

        cursorC = 0
        cursorR = 0
        for i in range(r) :
            for j in range(c) :
                res[i][j] = mat[cursorR][cursorC]
                if cursorC != len(mat[0]) - 1:
                    cursorC += 1
                else :
                    cursorC = 0
                    cursorR += 1
        return res