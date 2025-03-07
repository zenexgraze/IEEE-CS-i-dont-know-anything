# Creation of a Node
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to next node (initially None)
        self.prev = None  # Pointer to previous node (initially None)

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head of the list (Initially empty)

    def insert_at_head(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If list is empty, set head to new node
        else:
            new_node.next = self.head  # Link new node to the old head
            self.head.prev = new_node  # Update old head's prev
            self.head = new_node  # Update head to new node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:  # Traverse to the last node
                temp = temp.next
            temp.next = new_node  # Update last node’s next
            new_node.prev = temp  # Update new node’s prev

    def print_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ⇄ ")  # Print with arrows
            temp = temp.next
        print("None")


    def print_backward(self):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
        while temp.next:  # Move to last node
            temp = temp.next
        while temp:  # Traverse backward
            print(temp.data, end=" ⇄ ")
            temp = temp.prev
        print("None")

# Create a doubly linked list
dll = DoublyLinkedList()

# Insert nodes
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.insert_at_tail(30)

# Print the list
print("Forward Traversal:")
dll.print_forward()

print("Backward Traversal:")
dll.print_backward()


