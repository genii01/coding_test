# Q_13_palindrome-linked-list.py
# 연결 리스트가 팬린드롬 구조인지 판별하라
class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class solution :
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l3 = ListNode(2)
l4 = ListNode(1)
l2.next = l3
l3.next = l4

s = solution()
result = s.isPalindrome(l1)
print(result)


