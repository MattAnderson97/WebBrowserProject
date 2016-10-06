class Stack:
    def __init__(self):
        self.items = []
        self.maxSize = None
        self.stackPointer = None

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self,itemToAdd):
        if len(self.items) < self.maxSize:
            self.items.append(itemToAdd)
            if len(self.items) == 1:
                self.stackPointer = 0
            else:
                self.stackPointer += 1

    def pop(self):
        if len(self.items) > 0:
            item = self.items[self.stackPointer]
            self.items.pop(self.stackPointer)
            if self.stackPointer > 0:
                self.stackPointer -= 1
            else:
                self.stackPointer = None
            return item

    def peek(self):
        return self.items[self.stackPointer - 1]

    def size(self,maxSize):
        self.maxSize = maxSize
