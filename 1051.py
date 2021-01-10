class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        output = 0
        l = sorted(heights)
        while len(l) > 0:
            if heights.pop(0) != l.pop(0):
                output += 1
        return output
