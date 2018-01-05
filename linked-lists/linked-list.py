from node import Node

class LinkedList():
    def __init__(self, data):
        self.head = data

    def append(self, data):
        if self.head == null:
            self.head = Node(data)
            return

        current = self
        while(current.next != None):
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    def deleteWithValue(data):
        if self.head == null return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current != None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
