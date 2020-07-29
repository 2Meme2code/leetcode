class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        ds=[s]*len(indices)
        for i in range(0, len(s)):
            e=s[i]
            k=indices[i]
            ds[k]=e
        return string.join(ds,"")
