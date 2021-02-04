class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        target.sort()
        a = 0
        while a < len(target):
            if target[a] != arr[a]:
                a += 1
                return False
            elif target[a] == arr[a]:
                a += 1
        return True
