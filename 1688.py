class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.ans = 0
        def helper(n):
            if n <= 1:
                return
            if n % 2 == 0:
                self.ans += (n//2)
                helper(n//2)
            else:
                self.ans += n//2
                helper(1 + n//2)
        helper(n)
        return self.ans
