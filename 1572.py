class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        output = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:output += mat[i][j]
                elif (i + j) == (len(mat) - 1):output += mat[i][j]
        return output
