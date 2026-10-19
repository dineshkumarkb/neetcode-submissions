# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break

            group_next = kth.next

            # reverse nodes
            prev = kth.next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # reset group_prev from first to last node in the group
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next


    def getKthNode(self, node: ListNode, k: int):
        
        curr = node
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr


        

        