class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(A)
        even = []
        odd = []
        for i in range(n):
            if A[i] % 2 == 0:
                even.append(A[i])
            else:
                odd.append(A[i])
        return even + odd
        
