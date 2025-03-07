# Node Creation
class Doubly_Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data    # Store the data
        self.next = next    # Pointer to next node
        self.prev = prev    # Pointer to previous node


class Doubly_Linked_List:
    def __init__(self):
        self.head = None  # Head of the list which is initially empty

    def insert_at_head(self, data):
        new_node = Doubly_Node(data)  # Create a new node
        if self.head is None:
            self.head = new_node  # If list is empty, set head to new node
        else:
            new_node.next = self.head  # Link new node to the old head
            self.head.prev = new_node  # Update old head's prev
            self.head = new_node  # Update head to new node

    def insert_at_tail(self, data):
        new_node = Doubly_Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp_cursor = self.head
            while temp_cursor.next:  # Traverse to the last node
                temp_cursor = temp_cursor.next
            temp_cursor.next = new_node  # Update last node’s next
            new_node.prev = temp_cursor  # Update new node’s prev

    def print_forward(self):
        temp_cursor = self.head
        while temp_cursor:
            print(temp_cursor.data, end=" <-> ")  # Print with arrows
            temp_cursor = temp_cursor.next
        print("None")


    def print_backward(self):
        temp_cursor = self.head
        if temp_cursor is None:
            print("List is empty")
            return
        while temp_cursor.next:  # Move to last node
            temp_cursor = temp_cursor.next
        while temp_cursor:  # Traverse backward
            print(temp_cursor.data, end=" <-> ")
            temp_cursor = temp_cursor.prev
        print("None")

# Create a doubly linked list
dll = Doubly_Linked_List()

# Insert nodes
dll.insert_at_head(10)
dll.insert_at_head(20)
dll.insert_at_tail(30)

# Print the list
print("Forward Traversal:")
dll.print_forward()

print("Backward Traversal:")
dll.print_backward()
