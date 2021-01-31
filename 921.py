class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        output = [0]
        for i in S:
            if i == ')' and output[-1] == '(':
                output.pop()
            else:
                output.append(i)
        return len(output) -1
