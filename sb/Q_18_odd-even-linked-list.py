# %%
# Q_18_odd-even-linked-list.py
# 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라.

from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution :
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next :
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        
        return head
    
# l1_1 = ListNode(1)
# l1_2 = ListNode(2)
# l1_3 = ListNode(3)
# l1_4 = ListNode(4)
# l1_5 = ListNode(5)
l1_1 = ListNode(2)
l1_2 = ListNode(1)
l1_3 = ListNode(3)
l1_4 = ListNode(5)
l1_5 = ListNode(6)
l1_6 = ListNode(4)
l1_7 = ListNode(7)
l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5
l1_5.next = l1_6
l1_6.next = l1_7

s = Solution()
res = s.oddEvenList(l1_1)

while res :
    print(res.val)
    res = res.next


