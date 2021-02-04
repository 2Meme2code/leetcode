class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = collections.Counter(arr)
        return len(count) == len(set(count.values()))
