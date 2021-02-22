class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        presentIndexes = [i for i, val in enumerate(s) if val == c]
        return [min(abs(i - x) for x in presentIndexes) for i in range(0, len(s))]






































