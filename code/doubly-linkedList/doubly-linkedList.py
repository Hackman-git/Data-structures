class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
    def __repr__(self):
        return repr(self.value)


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ', '.join(nodes) + ']'

    def pushFront(self, value):
        newNode = Node(value=value, prev=None, next=self.head)
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
        if self.tail is None:
            self.tail = self.head

    def peekFront(self):
        return self.head

    def popFront(self):
        if self.head is None:
            print('empty list!')
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None
            return
        self.head.prev = None

    def pushBack(self, value):
        node = Node(value=value, next=None)
        if self.tail is None:
            self.head = node
            self.tail = node
            node.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def peekBack(self):
        return self.tail

    def popBack(self):
        if self.head is None:
            print('empty list!')
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def empty(self):
        return self.head is None

    def addAfter(self, node, value):
        node2 = Node(value=value, next=node.next)
        node2.prev = node
        node.next = node2
        if node2.next is not None:
            node2.next.prev = node2
        if self.tail == node:
            self.tail = node2

    def addBefore(self, node, value):
        node2 = Node(value=value, prev=node.prev, next=node)
        node.prev = node2
        if node2.prev is not None:
            node2.prev.next = node2
        if self.head == node:
            self.head = node2

    def find(self, value):
        current = self.head
        if current.value == value:
            return True
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def erase(self, value):
        if self.empty():
            print("list is empty!")
            return
        current = self.head
        if current.value == value:
            self.head = current.next
            self.head.prev = None
            return
        while current:
            if current.value == value:
                if current.next is None:
                    current.prev.next = None
                    self.tail = current.prev
                    return
                else:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                    return
            current = current.next
        print("key not in list!")


