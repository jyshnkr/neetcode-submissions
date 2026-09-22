class DynamicArray:
    
    def __init__(self, capacity: int):
    # Initialization
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity


    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
    # Check if length of array(number of elements filled) is at capacity(to hold)
    # then, call resize()
        if self.length == self.capacity:
            self.resize() 
    
    # Insert at next empty position
    # increment the length
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
    # check if the length is greater than 0
    # soft delete the last element
        if self.length > 0:
            self.length -= 1
    
    # return the popped element
        return self.arr[self.length]

    def resize(self) -> None:
    # Create the new array of double capacity
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity

    # Copy elements to new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity