class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        output_2 = []
        for row in A:
            temp = row[::-1]
            output.append(temp)

        for row_2 in output:
            output_3 = []
            for number in row_2:
                if number == 1:
                    output_3.append(0)
                else:
                    output_3.append(1)
            output_2.append(output_3)
        return output_2
