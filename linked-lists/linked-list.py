from node import Node

class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, data):
        if head == null:
            head = Node(data)
            return

        current = self
        while(current.next != None):
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        newHead = Node(data)
        newHead.next = head
        head = newHead
