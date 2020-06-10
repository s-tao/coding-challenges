import unittest

"""Palindrome: Implement a function to check if a linked list is a palindrome.

EXAMPLE:
Input: 1 -> 2 
Output: False

Input: 1 -> 2 -> 2 -> 1
Output: True
"""

class Node:
    """create node class"""

    def __init__(self, data):
        self.data = data
        self.next = None

    def is_palindrome(self, node):
        """check if linked list is a palindrome"""

        # O(n) space, uses stack and 2 runners
        stack = []
        
        slow = node
        fast = node
        
        if not fast or not fast.next:
            return True
        
        while fast and fast.next:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next
        
        while slow:
            if slow.data == stack[-1]:
                stack.pop()
            slow = slow.next
            
        return len(stack) == 0

        # O(n) space, uses array to loop backwards
        # track = []
        # curr = node

        # while curr:
        #     track.append(curr.data)
        #     curr = curr.next

        # for idx in range(len(track)-1, -1, -1):
        #     if track[idx] != node.data:
        #         return False
                
        #     node = node.next
        
        # return True

class Test(unittest.TestCase):
    """create test class"""

    def test_is_palindrome(self):
        """create linked list and test is_palindrome method"""

        ll_1 = Node(1)
        ll_1.next = Node(2)

        ll_2 = Node(1)
        ll_2.next = Node(2)
        ll_2.next.next = Node(2)
        ll_2.next.next.next = Node(1)

        res_1 = ll_1.is_palindrome(ll_1)
        self.assertFalse(res_1)

        res_2 = ll_2.is_palindrome(ll_2)
        self.assertTrue(res_2)
    
unittest.main(verbosity=2)

