class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        r=start
        for i in range(1,n):
            r=r^(start+2*i)
        return r
