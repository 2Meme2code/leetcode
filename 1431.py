class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        b=0
        a=[]
        for i in candies:
            candies[b]=candies[b]+extraCandies
            if max(candies)==candies[b]:
                a.append(True)
            else:
                a.append(False)
            candies[b]=candies[b]-extraCandies
            b=b+1
        return a
