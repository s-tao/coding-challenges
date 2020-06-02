"""Implement an algorithm to find the kth to last element of a singly linked 
list.
"""

class Node:
    """Create node class"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'<Node: node {self.data}>'

class LinkedList:
    """Create linked list"""

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

    
    def kth_to_last_element(self, k):
        """find kth to last element in linked list"""
        
        # space O(1)
        idx = 0
        curr = self.head
        while idx < k:
            if curr.next:
                curr = curr.next
            else:
                return None

            idx += 1
        
        curr_2 = self.head
        while curr:
            curr = curr.next
            curr_2 = curr_2.next
        
        return curr_2.data


        # space O(n)
        # position = {}
        # curr = self.head
        # count = 1
        
        # while curr:
        #     position[count] = curr.data
        #     count += 1
        #     curr = curr.next
            
        # find = len(position)+1 - k

        # return position.get(find)


ll = LinkedList()
ll.add_node('a')
ll.add_node('b')
ll.add_node('c')
ll.add_node('d')
ll.add_node('e')
ll.add_node('f')
ll.add_node('g')

ll.kth_to_last_element(3) # return e
ll.kth_to_last_element(10) # return None 
