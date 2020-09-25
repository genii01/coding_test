class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution :
    def isPalindrome(self,head:ListNode) -> bool:

        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev,rev.next,slow = slow,rev,slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow,rev = slow.next,rev.next

        return not rev


l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2

l3 = ListNode(2)
l4 = ListNode(1)
l2.next = l3
l3.next = l4

s = Solution()
print(s.isPalindrome(l1))