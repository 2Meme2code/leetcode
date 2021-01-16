class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output = []
        for num in range(left, right + 1):
	        if "0" not in str(num):
		        temp = num
		        while temp > 0:
			        r = temp % 10
			        if num % r != 0:
				        break
			        temp //= 10
		        else:
			        output.append(num)
        return output
