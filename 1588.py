class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        a = 1
        output = 0
        while a <= len(arr):
            for i in range(len(arr)):
                if i + a <= len(arr):
                    output += sum(arr[i:i + a])
            a += 2
            
        return output
