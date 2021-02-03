class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        output = []
        a = 0
        b = len(S)
        for i in S:
            if i == "I":
                output.append(a)
                a += 1
            else:
                output.append(b)
                b -= 1
        output.append(a)
        return output
