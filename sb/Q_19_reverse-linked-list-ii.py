
# %%
# Q_19_reverse-linked-list-ii.py
# 인덱스 m에서 n가지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.

from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def printNode(head: ListNode) -> None:
    while head:
        print(head.val)
        head = head.next

class Solution :
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m == n :
            return head

        root = start = ListNode(None)
        root.next = head
        
        for _ in range(m-1) :
            start = start.next
        end = start.next

        for _ in range(n-m) : 
            temp, start.next, end.next = start.next,end.next, end.next.next
            start.next.next = temp
            
        res = root.next
        
        return head

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
res = s.reverseBetween(l1_1, 2, 5)
printNode(res)

