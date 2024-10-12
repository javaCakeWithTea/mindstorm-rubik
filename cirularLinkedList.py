# Python Program of Traversal of Circular Linked List
class Node:
    def __init__(self, data):
        # Initialize a node with data and next pointer
        self.data = data
        self.next = None

class CircularLinkedList:
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
        


    def __eq__(self, value):
        return self.head == value.head
    
    def traverse(self):
        nodeValueDictionary = {}
        if not self.head:
            print("Circular Linked List is empty")
            return
        current = self.head
        while True:
            nodeValueDictionary[current.data]=current.next.data
            current = current.next
            if current == self.head:
                # Break the loop when we reach the head again
                return nodeValueDictionary
            
    def __eq__(self,value):
        ## Traverse and display the elements of the circular linked list
        ## For unique values in the circular linked list. The adjacents will be unique.
        ## So a dictionary of current value and next value can be used for comparison.
        ## Will always have 4 so don't worry about empty checks.
        return dict(sorted(self.traverse().items(),key=lambda item:item[1])) == dict(sorted(value.traverse().items(),key=lambda item:item[1]))

# Driver Code
#circular_list = CircularLinkedList()
#circular_list.append(1)
#circular_list.append(2)
#circular_list.append(3)

#print("Traversing Circular Linked List:")
#circular_list.traverse()