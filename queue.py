class Queue:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return len(self.item) ==0

    def enqueue(self,x):
        self.item.append(x)

    def dequeue(self):
        self.item.pop(0)

    def peek(self):
        return self.item[0]

    def size(self):
        return len(self.item)

    def clear(self):
        self.item = []


