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

        # create copy nodes in the first pass
        curr = head
        while curr:
            copy_node = Node(curr.val)
            copy_dict[curr] = copy_node
            curr = curr.next

        # assign next and random pointers to the copy node
        curr = head
        while curr:
            copy_node = copy_dict[curr]
            copy_node.next = copy_dict[curr.next]
            copy_node.random = copy_dict[curr.random]
            curr = curr.next

        return copy_dict[head]
        