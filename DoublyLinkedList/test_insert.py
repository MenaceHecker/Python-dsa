import unittest

from insert import DoublyLinkedList


def list_forward(dll):
    values = []
    node = dll.head
    while node:
        values.append(node.value)
        node = node.next
    return values


def list_backward(dll):
    values = []
    node = dll.tail
    while node:
        values.append(node.value)
        node = node.prev
    return values


class TestDoublyLinkedListInsert(unittest.TestCase):
    def test_insert_at_head(self):
        dll = DoublyLinkedList(2)
        dll.append(3)
        result = dll.insert(0, 1)
        self.assertTrue(result)
        self.assertEqual(dll.length, 3)
        self.assertEqual(list_forward(dll), [1, 2, 3])
        self.assertEqual(list_backward(dll), [3, 2, 1])
        self.assertIsNone(dll.head.prev)

    def test_insert_at_tail(self):
        dll = DoublyLinkedList(1)
        dll.append(2)
        result = dll.insert(2, 3)
        self.assertTrue(result)
        self.assertEqual(dll.length, 3)
        self.assertEqual(list_forward(dll), [1, 2, 3])
        self.assertEqual(list_backward(dll), [3, 2, 1])
        self.assertIsNone(dll.tail.next)

    def test_insert_in_middle(self):
        dll = DoublyLinkedList(1)
        dll.append(3)
        result = dll.insert(1, 2)
        self.assertTrue(result)
        self.assertEqual(dll.length, 3)
        self.assertEqual(list_forward(dll), [1, 2, 3])
        self.assertEqual(list_backward(dll), [3, 2, 1])

        middle = dll.head.next
        self.assertEqual(middle.value, 2)
        self.assertEqual(middle.prev.value, 1)
        self.assertEqual(middle.next.value, 3)

    def test_insert_invalid_index(self):
        dll = DoublyLinkedList(1)
        self.assertFalse(dll.insert(-1, 0))
        self.assertFalse(dll.insert(2, 3))
        self.assertEqual(dll.length, 1)
        self.assertEqual(list_forward(dll), [1])
        self.assertEqual(list_backward(dll), [1])


if __name__ == "__main__":
    unittest.main()
