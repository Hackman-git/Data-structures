class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if self.size() != 0:
            return self.items.pop()
        else: print('Queue is empty!')

    def size(self):
        return len(self.items)
