class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        if s.count('(') == 1: 
            return 1
        count = 0
        dep_count = 0
        for i in s:
            if i == "(" :
                count = count+1
            if i == ")":
                count = count-1
            dep_count = max(dep_count, count)
        return dep_count
