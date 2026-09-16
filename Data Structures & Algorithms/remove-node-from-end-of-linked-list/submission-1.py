# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)

        # init 2 pointers to track the nth node
        p1 = dummy
        p2 = head

        count = 0
        while count < n:
            p2 = p2.next
            count += 1

        # traverse till the end of the list
        while p2:
            p1 = p1.next
            p2 = p2.next

        # Now p1 is before the nth node
        p1.next = p1.next.next

        return dummy.next



        
        