class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        prev = 0
        output = (0, '')
        for key,time in zip(keysPressed, releaseTimes):
            output = max(output, (time-prev, key))
            prev = time
        return output[1]
