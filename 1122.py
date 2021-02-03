class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        output = []
        count = Counter(arr1)
        for i in range(len(arr2)):
            output += [arr2[i]] * count[arr2[i]]
        for i in output:
            arr1.remove(i)
        return output + sorted(arr1)
