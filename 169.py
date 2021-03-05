class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = nums[0] 
        c = 1
        for i in range(1, len(nums)):
            if nums[i] == output:
                c += 1 
            else:
                c -= 1
                if c == 0:
                    output = nums[i]
                    c = 1
        return output
