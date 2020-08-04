class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=0
        b=1
        c=[]
        for i in range(len(nums)/2):
            freq=nums[a]
            val=nums[b]
            for j in range(freq):
                c.append(val)
            a=a+2
            b=a+1
        return c
