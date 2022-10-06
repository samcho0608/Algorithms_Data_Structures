class Solution :
    def generate(self, numRows) :
        # without using the combinatoric equation
        pascal = [[1]]
        for i in range(1, numRows) :
            row = []
            for j in range(i+1) :
                if j == 0 :
                    row.append(pascal[i-1][j])  
                elif j >= i :
                    row.append(pascal[i-1][j-1])
                else :
                    row.append(pascal[i-1][j-1] + pascal[i-1][j])
            pascal.append(row)
        return pascal