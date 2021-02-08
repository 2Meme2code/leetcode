class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(i for i, j in Counter(nums).items() if j == 1)
