class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        a = []
        for i, box in enumerate(boxes):
            if box == '1':
                a.append(i)
        output = []
        for i in range(len(boxes)):
            n_step = sum([abs(n - i) for n in a])
            output.append(n_step)
        return output
