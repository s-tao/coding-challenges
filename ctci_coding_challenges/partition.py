"""Write code to partition a linked list around a value x, such that all nodes 
less than x come before all nodes greater than or equal to x. lf x is contained 
within the list, the values of x only need to be after the elements less than x 
(see below).The partition element x can appear anywhere in the "right 
partition"; it does not need to appear between the left and right partitions.

EXAMPLE:

# Input : 1->4->3->2->5->2->3, partition = 3

# Output: 1->2->2->3->3->4->5

"""

class Node:
    """Create node class"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Create linked list class"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        """Add new node to linked list"""

        new_node = Node(data)

        if not self.head:
            self.head = new_node

        if self.tail:
            self.tail.next = new_node

        self.tail = new_node

    def print_linkedlist(self):
        """Print linked list to confirm partitioned successfully"""
        
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next
        

    def partition(self, x):
        """Partition linkedlist per instructions"""

        partition_ll = less_than = LinkedList()
        greater_than = LinkedList()
        equal_to = LinkedList()

        curr = self.head
        
        while curr:
            if curr.data < x:
                less_than.add_node(curr.data)
            
            elif curr.data == x:
                equal_to.add_node(curr.data)

            else:
                greater_than.add_node(curr.data)

            curr = curr.next
            
        equal_curr = equal_to.head
        greater_curr = greater_than.head

        while equal_curr:
            less_than.add_node(equal_curr.data)
            equal_curr = equal_curr.next

        while greater_curr:
            less_than.add_node(greater_curr.data)
            greater_curr = greater_curr.next

        return partition_ll

# create linkedlist testcase 
ll = LinkedList()
ll.add_node(1)
ll.add_node(4)
ll.add_node(3)
ll.add_node(2)
ll.add_node(5)
ll.add_node(2)
ll.add_node(3)

# run partition method and print partition result
res = ll.partition(3)
res.print_linkedlist() # res: 1->2->2->3->3->4->5

