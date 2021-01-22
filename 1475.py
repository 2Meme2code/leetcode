class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res, stack = [], [0]
        for x in prices[::-1]:
            while x < stack[-1]: stack.pop()
            res += [x - stack[-1]]
            stack += [x]
        return res[::-1]
