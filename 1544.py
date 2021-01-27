class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = []
        for i in s:
            if not output:
                output.append(i)
            else:
                if output[-1].upper() == i.upper() and output[-1] != i:
                    output.pop()
                else:
                    output.append(i)
        return ''.join(output)
            
