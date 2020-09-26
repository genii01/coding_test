class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution :
    def mergeTwoLists(self,l1:ListNode,l2:ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1,l2 = l2,l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next,l2)
        return l1


l1 = ListNode(1)
l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1.next = l1_1
l1_1.next = l1_2

l2 = ListNode(1)
l2_1 = ListNode(3)
l2_2 = ListNode(4)
l2.next = l2_1
l2_1.next = l2_2


s = Solution()
result = s.mergeTwoLists(l1,l2)
while result.next :
    print(result.val)
    result = result.next