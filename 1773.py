class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        rules = {'type' : 0, 'color' : 1, 'name' : 2}
        output = 0
        for i in items:
            if i[rules[ruleKey]] == ruleValue:
                output += 1
        return output
