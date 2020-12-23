class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            stop = 0
            for i in word:
                if i not in allowed:
                    stop += 1
            if stop == 0:
                count += 1
                
        return count
