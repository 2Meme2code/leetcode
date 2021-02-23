class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        even = n - 1
        characters = ['a','b']
        output = ''
        if n % 2 != 0:
            output = characters[0] * n
        else:
            output = characters[0] * even + characters[1]
        return output
