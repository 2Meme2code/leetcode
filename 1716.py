class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        output = x = 0
        for i in range(n): 
            if i % 7 == 0: x += 1
            output += x + i % 7
        return output 
