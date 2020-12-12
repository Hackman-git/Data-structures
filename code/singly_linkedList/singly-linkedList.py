class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

    def __repr__(self):
        return repr(self.key)


class SinglyLinkedList:
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

    def pushFront(self, key):
        self.head = Node(key=key, next=self.head)
        if self.tail is None:
            self.tail = self.head

    def peekFront(self):
        return self.head

    def popFront(self):
        if self.empty():
            print('empty list!')
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def pushBack(self, key):
        node = Node(key=key, next=None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def peekBack(self):
        return self.tail

    def popBack(self):
        if self.empty():
            print('empty list!')
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            p = self.head
            while p.next.next is not None:
                p = p.next
            p.next = None
            self.tail = p

    def empty(self):
        return self.head is None

    def addAfter(self, node, key):
        node2 = Node(key=key)
        node2.next = node.next
        node.next = node2
        if self.tail == node:
            self.tail = node2

    def addBefore(self, node, key):
        node2 = Node(key=key)
        if self.head == node:
            self.head = node2
            node2.next = node
        else:
            current = self.head
            while current.next != node:
                current = current.next
            current.next = node2
            node2.next = node

    def find(self, key):
        current = self.head
        if current.key == key:
            return True
        while current is not None:
            if current.key == key:
                return True
            current = current.next
        return False

    def erase(self, key):
        if self.empty():
            print("list is empty!")
            return
        current = self.head
        prev = None
        while current and current.key != key:
            prev = current
            current = current.next
        if prev is None:
            self.head = current.next
        elif current:
            prev.next = current.next
            current.next = None
        else: print("key not found!")

