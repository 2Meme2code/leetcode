class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
    s.sort()
        output = 0
        for i in s:
            if i >= g[output]:
		output += 1
	    	if output == len(g):
		    break
        return output
