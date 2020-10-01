class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution :
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next # 2 4 6
            head.next = self.swapPairs(p.next) # 4 6 None
            p.next = head
            return p
        return head

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

s = Solution()
result = s.swapPairs(l1)
while result :
    print(result.val)
    result = result.next