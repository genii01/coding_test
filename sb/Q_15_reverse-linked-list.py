
# Q_15_reverse-linked-list.py
# 연결리스트를 뒤집어라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution :
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node :
            next, node.next = node.next , prev
            prev, node = node, next
        
        return prev
        
l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_4 = ListNode(4)
l1_5 = ListNode(5)
l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5


s = Solution()
res = s.reverseList(l1_1)
while res :
    print(res.val)
    res = res.next


