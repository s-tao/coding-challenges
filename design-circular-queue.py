import unittest

class CircularQueue:
    """Implement a circular queue"""

    def __init__(self, k: int):
        """Initialize queue with k as the size"""
        self.queue = []
        self.size = k


    def enQueue(self, value):
        """Insert element into circular queue, return true if successfull"""
        
        if not self.isFull():
            self.queue.append(value)
            return True

        else:
            return False


    def deQueue(self):
        """Remove element from circular queue, return true if successfull"""

        if not self.isEmpty():
            self.queue.pop(0)
            return True

        else:
            return False


    def front(self):
        """Return first element in queue"""

        if not self.isEmpty():
            return self.queue[0]
        else:
            return -1


    def back(self):
        """Return last element in queue"""

        if not self.isEmpty():
            return self.queue[-1]
        
        else:
            return -1


    def isEmpty(self):
        """Return true if circular queue is empty"""

        return len(self.queue) == 0


    def isFull(self):
        """Return true if circular queue is full"""

        return len(self.queue) == self.size


class Test(unittest.TestCase):

    def test_initialize_circular_queue(self):
        """Test initialize CircularQueue is successfull"""
        c_queue = CircularQueue(3)
        self.assertEqual(c_queue.size, 3)
    

    def test_enQueue(self):
        """Test should successfully add new element onto circular queue when it 
        is not full
        """
        c_queue = CircularQueue(1)
        result_1 = c_queue.enQueue(2)
        self.assertEqual(result_1, True)

        # test when CircularQueue is full
        result_2 = c_queue.enQueue(4)
        self.assertEqual(result_2, False)


    def test_deQueue(self):
        """Test should successfully remove element from circular queue if it is
        not empty and return -1 if empty
        """

        c_queue = CircularQueue(3)
        param = c_queue.enQueue(5)
        result_1 = c_queue.deQueue()
        self.assertEqual(result_1, True)

        # test when CircularQueue is empty
        result_2 = c_queue.deQueue()
        self.assertEqual(result_2, False)


    def test_front(self):
        """Test should successfully returns first element in circular queue"""

        c_queue = CircularQueue(3)
        param = c_queue.enQueue(1)
        param2 = c_queue.enQueue(4)
        result = c_queue.front()
        self.assertEqual(result, 1)

        # test return -1 when circular queue is empty
        c_queue2 = CircularQueue(3)
        result = c_queue2.front()
        self.assertEqual(result, -1)


    def test_back(self):
        """Test should successfully return last element in circular queue"""

        c_queue = CircularQueue(3)
        param = c_queue.enQueue(5)
        param2 = c_queue.enQueue(2)
        result = c_queue.back()
        self.assertEqual(result, 2)

        # test return -1 when circular queue is empty
        c_queue2 = CircularQueue(3)
        result = c_queue2.back()
        self.assertEqual(result, -1)


    def test_isEmpty(self):
        """Test should return True when Circular Queue is empty and vice versa
        """

        c_queue = CircularQueue(2)
        result = c_queue.isEmpty()
        self.assertEqual(result, True)

        # test should return False b/c Circular Queue is not empty
        param = c_queue.enQueue(3)
        result = c_queue.isEmpty()
        self.assertEqual(result, False)

    
    def test_isFull(self):
        """Test should return True when circular queue is full and False when
        it is not full"""

        c_queue = CircularQueue(2)
        param = c_queue.enQueue(3)
        result = c_queue.isFull()
        self.assertEqual(result, False)

        param2 = c_queue.enQueue(5)
        result_2 = c_queue.isFull()
        self.assertEqual(result_2, True)


unittest.main(verbosity=2)