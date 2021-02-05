class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        a = 0
        output = 0
        for i in sorted(boxTypes, key = lambda x: x[1], reverse = True):
            if a + i[0] <= truckSize:
                a += i[0]
                output += i[0] * i[1]
            else: 
                output += (truckSize - a) * i[1]
                a += truckSize - a
                break
        return output
