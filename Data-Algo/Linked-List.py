#! python3
# LinkedList Implementation

class LinkedList:

    def __init__(self):
        self.head: self.Node = None
    
    def append(self, data) -> None:
        new: self.Node = self.Node(data)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new

    def printList(self) -> None:
        current = self.head
        while current:
            print(current.data)
            current = current.next

    class Node:

        def __init__(self, data):
            self.data = data
            self.next: self.Node = None

# Create an example Linked List
list = LinkedList()

# Assign it three nodes with the values 1, 2, and 3
list.append(1)
list.append(2)
list.append(3)

# Print values of List
list.printList()