class Solution :
    def isValidSudoku(self, board) :
        # row 1~9
        # col 1~9
        # subbox 1~9
        coord = {
            f"{n}" : []
            for n in range(1,10)
        }

        for i in range(9) :
            for j in range(9) :
                num = board[i][j]
                if num != "." :
                    coord[num].append((i,j))
        
        for numCoords in coord.values() :
            cols = [c[1] for c in numCoords]
            if len(cols) != len(set(cols)) :
                return False
            rows = [c[0] for c in numCoords]
            if len(rows) != len(set(rows)) :
                return False
            subBoxes = [(c[0] // 3) + c[1] // 3 * 3 for c in numCoords]
            if len(subBoxes) != len(set(subBoxes)) :
                return False

        return True