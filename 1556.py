class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        output= str()
        ans = list(str(n))
        ans.reverse()
        i = 3
        while i < len(ans):
            ans.insert(i,".")
            i += 4
        ans.reverse()
        for k in ans:
            output += k
        return output
