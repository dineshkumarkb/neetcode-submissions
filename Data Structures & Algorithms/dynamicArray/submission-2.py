class DynamicArray:
    
    def __init__(self, capacity: int):
        self.my_array = [0] * capacity
        self.capacity = capacity
        self.size = 0
        


    def get(self, i: int) -> int:
        if i < len(self.my_array):
            return self.my_array[i]


    def set(self, i: int, n: int) -> None:
        if i < len(self.my_array):
            self.my_array[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.my_array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        if len(self.my_array) > 0:
            self.size -= 1
            return self.my_array[self.size]
           
 

    def resize(self) -> None:
        self.capacity *= 2 
        new_array = [0] * self.capacity
        for i in range(len(self.my_array)):
            new_array[i] = self.my_array[i]
        self.my_array = new_array


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity

