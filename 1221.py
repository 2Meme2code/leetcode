class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=b=c=0
        for i in s:
            if i == "L":
                b=b+1
            else:
                c=c+1
            if b==c:
                a=a+1
        return a
