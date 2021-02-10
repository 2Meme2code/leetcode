class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        output = 0
        for i in range(1, len(tiles) + 1):
            a = list(permutations(tiles, i))
            output += len(list(set(a)))
        return(output)
