class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        b=0
        a=[]
        while b<len(index):
            a.insert(index[b], nums[b])
            b=b+1
        return a
