class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        a=0
        while head:
            a=(a<<1)|head.val
            head=head.next
        return a
