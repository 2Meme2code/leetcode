class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l = min(len(word1), len(word2))
        if len(word1) > len(word2):
            w = word1
        else:
            w = word2
        output = ""
        for i in range(l):
            output += word1[i] + word2[i]
        return output + w[l:]
