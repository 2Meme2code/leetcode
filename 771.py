class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        a=0
        for i in J:
            for c in S:
                if i in c:
                    a=a+1
        return a
