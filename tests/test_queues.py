import unittest

from algorithms.queues import (
    ArrayQueue, LinkedListQueue,
    max_sliding_window,
    reconstruct_queue,
    PriorityQueue,
    moving_average,
    zigzagiterator
)


class TestQueue(unittest.TestCase):
    """
        Test suite for the Queue data structures.
    """

    def test_ArrayQueue(self):
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # test __iter__()
        it = iter(queue)
        self.assertEqual(1, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(3, next(it))
        self.assertRaises(StopIteration, next, it)

        # test __len__()
        self.assertEqual(3, len(queue))

        # test is_empty()
        self.assertFalse(queue.is_empty())

        # test peek()
        self.assertEqual(1, queue.peek())

        # test dequeue()
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())

        self.assertTrue(queue.is_empty())

    def test_LinkedListQueue(self):
        queue = LinkedListQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # test __iter__()
        it = iter(queue)
        self.assertEqual(1, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(3, next(it))
        self.assertRaises(StopIteration, next, it)

        # test __len__()
        self.assertEqual(3, len(queue))

        # test is_empty()
        self.assertFalse(queue.is_empty())

        # test peek()
        self.assertEqual(1, queue.peek())

        # test dequeue()
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())

        self.assertTrue(queue.is_empty())


class TestSuite(unittest.TestCase):
    def test_max_sliding_window(self):
        array = [1, 3, -1, -3, 5, 3, 6, 7]
        self.assertEqual(max_sliding_window(array, k=5), [5, 5, 6, 7])
        self.assertEqual(max_sliding_window(array, k=3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(max_sliding_window(array, k=7), [6, 7])

        array = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
        self.assertEqual(max_sliding_window(array, k=4), [10, 10, 10, 15, 15, 90, 90])
        self.assertEqual(max_sliding_window(array, k=7), [15, 15, 90, 90])
        self.assertEqual(max_sliding_window(array, k=2), [8, 10, 10, 9, 9, 15, 15, 90, 90])

    def test_reconstruct_queue(self):
        self.assertEqual([[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
                         reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    
    def test_moving_average(self):
        queue = moving_average.MovingAverage(5)
        self.assertEqual(queue.next(2), 2)
        self.assertEqual(queue.next(5), (5 + 2) / 2)
        self.assertEqual(queue.next(8), (2 + 5 + 8) / 3)
        self.assertEqual(queue.next(10), (2 + 5 + 8 + 10) / 4)


class TestPriorityQueue(unittest.TestCase):
    """Test suite for the PriorityQueue data structures.
    """

    def test_PriorityQueue(self):
        queue = PriorityQueue([3, 4, 1, 6])
        self.assertEqual(4, queue.size())
        self.assertEqual(1, queue.pop())
        self.assertEqual(3, queue.size())
        queue.push(2)
        self.assertEqual(4, queue.size())
        self.assertEqual(2, queue.pop())

class Testzigzagiterator(unittest.TestCase):
    """Test Suite for the zigzagiterator
    """

    def test_zigzagiterator(self):
        list1 = [1, 3, 5]
        list2 = [2, 4, 6]
        result = []
        iterator = zigzagiterator.ZigZagIterator(list1, list2)
        while iterator.has_next():
            result.append(iterator.next())
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])



if __name__ == "__main__":
    unittest.main()
