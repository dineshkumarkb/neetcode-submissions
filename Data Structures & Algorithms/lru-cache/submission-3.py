class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):

        self.cap = capacity
        self.cache = {}
        # init 2 nodes left and right
        # left always has the oldest cache
        # right always has the new cache
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # helper methods
    def remove(self, node: ListNode) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node: ListNode):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key=key, val=value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
     
        
