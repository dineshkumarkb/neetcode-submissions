"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copy_dict = {None: None}

        curr = head

        # create copy nodes
        while curr:
            copy_dict[curr] = Node(curr.val)
            curr = curr.next

        # assign next and random nodes
        curr = head
        while curr:
            copy = copy_dict[curr]
            copy.next = copy_dict[curr.next]
            copy.random = copy_dict[curr.random]
            curr = curr.next
        
        return copy_dict[head]
        