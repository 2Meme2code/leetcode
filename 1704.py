class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = 'aeiouAEIOU'
        a, b = s[:len(s) // 2], s[len(s) // 2:]
        return sum(ch in vowels for ch in a) == sum(ch in vowels for ch in b)
