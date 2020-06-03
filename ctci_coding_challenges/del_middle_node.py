"""
Delete Middle Node: Implement an algorithm to delete a node in the middle 
(i.e., any node but the first and last node, not necessarily the exact middle) 
of a singly linked list, given only access to that node.

EXAMPLE:
Input: the node c from the linked list a -> b -> c -> d -> e -> f
Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_node(self, data):
        """Add node to linked list"""

        new_node = Node(data)

        if not self.head:
            self.head = new_node
        
        if self.tail:
            self.tail.next = new_node
        
        self.tail = new_node

    def print_node(self):
        """Print all nodes in linked list to confirm results"""

        curr = self.head
        
        while curr:
            print(curr.data)
            curr = curr.next

    def del_middle_node(self):
        """Remove middle node from linked list without access to head node"""

        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            fast = fast.next.next

            if not fast:
                break

            prev = slow
            slow = slow.next

        prev.next = slow.next              


ll = LinkedList()
node_a = ll.add_node('a')
node_b = ll.add_node('b')
node_c = ll.add_node('c')
node_d = ll.add_node('d')
node_e = ll.add_node('e')
node_f = ll.add_node('f')
ll.print_node()
print('\n')
ll.del_middle_node()
ll.print_node()


