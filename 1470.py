class Solution(object):
    def shuffle(self, nums, n):
        i=0
        nums2=[]
        while i<n:
            nums2.append(nums[i])
            nums2.append(nums[n+i])
            i=i+1
        return nums2
