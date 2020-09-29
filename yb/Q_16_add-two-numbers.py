class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution :
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1 :
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry,val = divmod(sum+carry,10)
            head.next = ListNode(val)
            head = head.next

        return root.next

l1 = ListNode(2)
l1_1 = ListNode(4)
l1_2 = ListNode(3)
l1.next = l1_1
l1_1.next = l1_2

l2 = ListNode(5)
l2_1 = ListNode(6)
l2_2 = ListNode(4)
l2.next = l2_1
l2_1.next = l2_2

s = Solution()
result = s.addTwoNumbers(l1,l2)
while result :
    print(result.val)
    result = result.next