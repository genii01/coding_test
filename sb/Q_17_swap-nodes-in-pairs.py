# %%
# Q_17_swap-nodes-in-pairs.py
# 역순으로 저장된 연결 리스트의 숫자를 더하라.

from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution :
    def swapPairs(self, head: ListNode) -> ListNode:
        head1 = head
        while head1 and head1.next :
            head1.val, head1.next.val = head1.next.val, head1.val
            head1 = head1.next.next
        
        return head
    
l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_4 = ListNode(4)
l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4

s = Solution()
res = s.swapPairs(l1_1)

while res :
    print(res.val)
    res = res.next


