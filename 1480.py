class Solution(object):
    def runningSum(self, nums):
        a=0
        sum=[]
        for i in nums:
            sum.append(a+i)
            a=a+i
            
        return sum
