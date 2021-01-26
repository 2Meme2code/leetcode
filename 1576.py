class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        q = s.count('?')
        arr = list(map(chr, range(97, 123)))*q
        for c in s:
            if c in arr:
                for i in range(q):
                    arr.remove(c)
        st = ""
        for idx, c in enumerate(s):
            if c == '?':
                st+=arr.pop()
            else:
                st+=c
        return st
