class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        count = 0

        curr = self.head.next

        # Move curr to ith node
        while curr:

            if count == index:
                return curr.val
            count += 1
            curr = curr.next

        return -1

        

    def insertHead(self, val: int) -> None:

        new_node = Node(val)

        # handle when the list is empty
        if not self.head.next:
            self.tail = new_node

        new_node.next = self.head.next
        self.head.next = new_node
        

    def insertTail(self, val: int) -> None:

        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        

    def remove(self, i: int) -> bool:

        curr = self.head

        count = 0

        while curr and count < i:
            count += 1
            curr = curr.next

        if curr and curr.next:
            # handle tail node removal
            if curr.next == self.tail:
                self.tail = curr

            curr.next = curr.next.next
            return True

        return False

        

    def getValues(self) -> List[int]:

        res = []

        current = self.head.next

        while current:
            res.append(current.val)
            current = current.next

        return res
        
