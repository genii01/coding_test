# %%
# Q_16_add-two-numbers.py
# 역순으로 저장된 연결 리스트의 숫자를 더하라.

from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution :
    def reverseList(self, head1: ListNode) -> ListNode:
        node1, prev1 = head1, None
        while node1 :
            next, node1.next = node1.next , prev1
            prev1, node1 = node1, next
        
        return prev1
    
    def toList(self, node: ListNode) -> List :
        list1 = []
        while node :
            list1.append(node.val)
            node = node.next
        return list1
    
    def toReverseLinkedList(self, l1 : List) -> ListNode:
        prev = None
        for i in c:
            node = ListNode(i)
            node.next = prev
            prev = node
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode :
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b)) 

        return self.toReverseLinkedList(str(resultStr))

l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

s = Solution()
res = s.addTwoNumbers(l1_1, l2_1)

while res :
    print(res.val)
    res = res.next
