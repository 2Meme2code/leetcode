class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=10
        b=[]
        c=0
        d=0
        b.append(nums[d]%10)
        if len(b)%2==0:
            c=c+1
            d=d+1
        while d<len(nums):
            b=[]
            e=1
            while e<=nums[d]:
                b.append(nums[d]/a%10)
                e=e*10
            a=a*10
            d=d+1
            if len(b)%2==0:
                c=c+1
        return c
