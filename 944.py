class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        return sum(tuple(sorted(a)) != a for a in zip(*strs))
