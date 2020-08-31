class RingBuffer:
    def __init__(self, capacity =10):
        # set default capacity to 10
        self.capacity = capacity
        self.size = 0 #Size starts at 0
        self.write_index = 0 #write index writes at first part of the storage array, position 0
        self.storage = [] #Storage is empty array/list

    def append(self, item):

        #If the size of the ring with input is greater than the capacity, write the index at 0
        if self.size >= self.capacity:
            self.storage[self.write_index] = item
        else: #Otherwise append it and increase size by 1
            self.storage.append(item)
            self.size += 1
        #if the write index is less than the capacity -1, write index +1
        if self.write_index < (self.capacity - 1):
            self.write_index += 1
        else: # Otherwise perform at start of list 0
            self.write_index = 0

    def get(self):
        #return the storage list/array
        return self.storage