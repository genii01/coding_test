class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution :
    def reverseList(self,head:ListNode) -> ListNode:
        node,prev = head,None
        while node :
            next, node.next = node.next , prev
            prev, node = node, next
        return prev


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

s = Solution()
result = s.reverseList(l1)
while result :
    print(result.val)
    result = result.next