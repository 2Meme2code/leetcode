class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A[::2], A[1::2] = [a2 for a2 in A if not a2 & 1], [a2 for a2 in A if a2 & 1]
        return A
