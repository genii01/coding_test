class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution :
    def reverseBetween(self, head: ListNode, m:int, n:int) -> ListNode:
        if not head or m == n :
            return head

        root = start = ListNode(None)
        root.next = head

        for _ in range(m-1):
            start = start.next
        end = start.next

        for _ in range(n-m):
            tmp,start.next,end.next = start.next,end.next,end.next.next
            start.next.next = tmp

        return root.next

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

m , n = 2 , 5

s = Solution()
result = s.reverseBetween(l1,m,n)
while result :
    print(result.val)
    result = result.next