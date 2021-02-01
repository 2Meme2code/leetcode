class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt = gain
        alt.insert(0, 0)
        new_alt = []
        a = 0
        for i in alt:
            a += i
            new_alt.append(a)
        return max(new_alt)
