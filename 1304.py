class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        res = []
        if n % 2 != 0:
            n = n - 1
            res.append(0)
        for i in range(1, (n // 2) + 1):
            res.append(i)
            res.append(-i)
        return res
    
