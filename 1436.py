class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        return (set([path[1] for path in paths]) - set([path[0] for path in paths])).pop()
