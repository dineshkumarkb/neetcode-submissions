class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    
    def get(self, index: int) -> int:
        current = self.head.next
        count = 0

        while current:
            if index == count:
                return current.val
            count += 1
            current = current.next

        return -1

        

    def insertHead(self, val: int) -> None:

        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

        if not new_node.next:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:

        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:

        current = self.head
        count = 0

        while count < index:
            count += 1
            current = current.next
        
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        
        return False
        

    def getValues(self) -> List[int]:

        res = []

        current = self.head.next

        while current:
            res.append(current.val)
            current = current.next

        return res
        
