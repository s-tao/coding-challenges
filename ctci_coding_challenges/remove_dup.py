"""Write code to remove duplicates from an unsorted linked list. 
FOLLOW UP: How would you solve this problem if a temporary buffer is not 
allowed?
"""

class Node:
    """Create node"""

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):

        return f'<Node: Node {self.data}>'

class LinkedList:
    """LinkedList"""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        """add node to linked list"""

        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        
        if self.tail:
            self.tail.next = new_node
        
        self.tail = new_node


    def remove_dup(self):
        """remove duplicates in linked list"""

        # solution uses hashset O(n) space
        # seen = set(self.head.data)
        # curr = self.head

        # while curr:
        #     if curr.next:
        #         if curr.next.data not in seen:
        #             seen.add(curr.next.data)
        #         else:    
        #             curr.next = curr.next.next
            
        #     curr = curr.next

        # solution uses constant space O(1), with runtime O(n^2)
        slow = fast = self.head

        while slow:
            while fast.next:
                if fast.next.data == slow.data:
                    fast.next = fast.next.next
                else:
                    fast = fast.next

            # slow = slow.next
            # fast = slow
            slow = fast = slow.next

    def print_node(self):
        """print each node in linked list"""

        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next


# create dummy linkedlist 
ll = LinkedList()
a = ll.add_node('a')
d = ll.add_node('d')
c = ll.add_node('c')
a_2 = ll.add_node('a')
b = ll.add_node('b')
c_2 = ll.add_node('c')
c_3 = ll.add_node('c')

ll.remove_dup()