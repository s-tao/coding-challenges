"""Sum Lists: You have two numbers represented by a linked list, where each node 
contains a single digit. The digits are stored in reverse order, such that the 
1's digit is at the head of the list. Write a function that adds the two numbers 
and returns the sum as a linked list.

EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295. 
Output: (2 -> 1 -> 9). That is 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is 617 + 295. 
Output: (9 -> 1 -> 2). That is 912.
"""

class Node:
    """Create node class"""

    def __init__(self, data):
        self.data = data
        self.next = None
    

def sum_linkedlist(num_1, num_2):
    """Find sum of linked list when in reverse order"""
    carry = 0
    total = Node(0)
    total_tail = total

    while num_1 and num_2:
        res = num_1.data + num_2.data + carry
        if res > 9:
            new_node = Node(res%10)
            carry = 1

        else:
            new_node = Node(res)
            carry = 0

        total_tail.next = new_node
        total_tail = total_tail.next

        num_1, num_2 = num_1.next, num_2.next

    while num_1 and not num_2:
        res = num_1.data + carry
        if res > 9:
            new_node = Node(res%10)
            carry = 1

        else:
            new_node = Node(res)
            carry = 0
        
        total_tail.next = new_node
        total_tail = total_tail.next
        
        num_1 = num_1.next

    while num_2 and not num_1:
        res = num_2.data + carry
        if res > 9:
            new_node = Node(res%10)
            carry = 1

        else:
            new_node = Node(res)
            carry = 0
            
        total_tail.next = new_node
        total_tail = total_tail.next
        num_2 = num_2.next
    
    if carry:
        new_node = Node(1)
        total_tail.next = new_node
        total_tail = total_tail.next

    # print total result to confirm sum is correct
    curr_res = total.next
    while curr_res:
        print(curr_res.data)
        curr_res = curr_res.next



# testcase: digits stored in reverse order
r_num_1 = Node(7)
r_num_1.next = Node(1)
r_num_1.next.next = Node(6)

r_num_2 = Node(5)
r_num_2.next = Node(9)
r_num_2.next.next = Node(2)

sum_linkedlist(r_num_1, r_num_2) # 219

# testcase: digits stored in forward order 
f_num_1 = Node(6)
f_num_1.next = Node(1)
f_num_1.next.next = Node(7)

f_num_2 = Node(2)
f_num_2.next = Node(9)
f_num_2.next.next = Node(5)

# sum_linkedlist(f_num_1, f_num_2) # 912