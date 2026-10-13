# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)

        # init 2 pointers to find the nth node
        p1 = dummy
        p2 = dummy.next

        while p2 and n > 0:
            p2 = p2.next
            n -= 1

        while p2:
            p1 = p1.next
            p2 = p2.next

        prev = p1
        prev.next = prev.next.next

        return dummy.next
