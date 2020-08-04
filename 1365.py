class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2=[]
        for i in nums:
            a=0
            b=0
            for j in nums:
                if i>nums[a]:
                    b=b+1
                a=a+1
            nums2.append(b)
        return nums2
