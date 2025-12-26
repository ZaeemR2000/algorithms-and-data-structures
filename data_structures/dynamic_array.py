class DynamicArray:

    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self._len = 0
    

    def validate_index(self, index):
        if not (0 <= index <= self._len):
            raise IndexError("given index is out of bound")
        
    def is_empty(self):
        if self._len == 0:
            return True
        return False
    

    def length(self): 
        return self._len


    def append(self, value):
        self.resize()
        self.array[self._len] = value
        self._len += 1
        

    def resize(self):
        if self._len != self.capacity:
            return
        self.capacity = self.capacity * 2
        resized_array = [None] * self.capacity

        for i in range(self._len):
            resized_array[i] = self.array[i]
        self.array = resized_array

    
    def insert(self, value, index):
        self.validate_index(index=index)
        self.resize()

        for i in range(self._len-1, index-1, -1):
            self.array[i+1] = self.array[i]
        
        self.array[index] = value
        self._len += 1


    def index_at(self, index):
        self.validate_index(index=index)
        return self.array[index]
    

    def remove(self, index):
        self.validate_index(index=index)
        for i in range(index, self._len-1, 1):
            self.array[i] = self.array[i+1]
        self._len -= 1
        self.array[self._len-1] = None
