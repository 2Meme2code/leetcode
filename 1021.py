class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        a = 1
        output = ''
        for i in S:
            if i == '(':
                a -= 1
                if a != 0:
                    output += i
            elif i == ')':
                a += 1
                if a <= 0:
                    output += i
        return output
