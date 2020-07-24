class Solution(object):
    def numIdenticalPairs(self, nums):
        good_pair=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j] and i<j:
                    good_pair=good_pair+1
                        
        return good_pair
