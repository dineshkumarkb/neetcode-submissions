class MinStack:

    def __init__(self):
        self.stack = [] #(min, val)

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            curr_min = min(self.stack[-1][0], val)
            self.stack.append((curr_min, val))
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
         return self.stack[-1][1]
        

    def getMin(self) -> int:
        return self.stack[-1][0]
        
        
