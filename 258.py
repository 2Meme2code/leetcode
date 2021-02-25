class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        output = str(num)
        while len(output) > 1:
            output = str(sum([int(i) for i in output]))
        return int(output)
