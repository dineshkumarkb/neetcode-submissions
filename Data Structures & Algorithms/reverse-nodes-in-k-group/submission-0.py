# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy # one node before the start of the group

        while True:

            kth = self.getKth(group_prev, k)
            if not kth:
                break

            group_next = kth.next
            
            # reverse the nodes
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next




    
    # function to get Kth    
    def getKth(self, node, k):

        curr = node

        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr

        