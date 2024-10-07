# Python Program of Traversal of Circular Linked List
class Node:
    def __init__(self, data):
        # Initialize a node with data and next pointer
        self.data = data
        self.next = None

class CircularLinkedList:

    nodeStore={}

    def __init__(self):
        # Initialize an empty circular linked list with head pointer pointing to None
        self.head = None

    def append(self, data):
        # Append a new node with data to the end of the circular linked list
        new_node = Node(data)
        if not self.head:
            # If the list is empty, make the new node point to itself
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                # Traverse the list until the last node
                current = current.next
            # Make the last node point to the new node
            current.next = new_node
            # Make the new node point back to the head
            new_node.next = self.head

        self.nodeStore.add(new_node)

    def __eq__(self, value) -> bool:
        self.nodeStore == object.nodeStore

# Driver Code
#circular_list = CircularLinkedList()
#circular_list.append(1)
#circular_list.append(2)
#circular_list.append(3)

#print("Traversing Circular Linked List:")
#circular_list.traverse()