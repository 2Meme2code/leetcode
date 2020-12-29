class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_list = nums
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    first_index = target_list.index(nums[i])
                    if first_index == len(nums):
                        return(first_index , first_index + 1)
                    else:
                        return [first_index , target_list.index(nums[j],first_index + 1)]
