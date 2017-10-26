'''
    Tests to test Linked List class
'''

import unittest

from app.linkedlist import LinkedList
from app.node import Node


class TestLinkedList(unittest.TestCase):
    '''
        Test class to test Linked List class
    '''
    def setUp(self):
        self.linkedlist = LinkedList()

    def test_empty_list(self):
        '''
            Tests Empty list is created
        '''
        self.assertIsInstance(self.linkedlist, LinkedList)

    def test_insert_at_head(self):
        '''
            This will test element can be inserted at the start of the list
        '''
        self.linkedlist.insert(4)
        self.assertEqual(self.linkedlist.get_node_count(), 1)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)

    def test_insert_at_tail(self):
        '''
            This will test element can be appended to the list
        '''
        self.linkedlist.insert(4)
        self.assertEqual(self.linkedlist.get_node_count(), 1)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.linkedlist.append_to_list(5)
        self.assertEqual(self.linkedlist.get_node_count(), 2)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.assertEqual(self.linkedlist.get_value_at_index(1), 5)

    def test_insert_element_at_index(self):
        '''
            Tests elements are inserted at given index
        '''
        self.linkedlist.insert(4)
        self.assertEqual(self.linkedlist.get_node_count(), 1)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.linkedlist.append_to_list(6)
        self.assertEqual(self.linkedlist.get_node_count(), 2)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.assertEqual(self.linkedlist.get_value_at_index(1), 6)
        self.linkedlist.insert_at_index(5, 1)
        self.assertEqual(self.linkedlist.get_node_count(), 3)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.assertEqual(self.linkedlist.get_value_at_index(1), 5)
        self.assertEqual(self.linkedlist.get_value_at_index(2), 6)

    def test_insert_element_at_zero(self):
        '''
            Tests elements are inserted at index zero using insert_at_index.
            Indicating insert behaviour
        '''
        self.linkedlist.insert_at_index(4, 0)
        self.assertEqual(self.linkedlist.get_node_count(), 1)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)

    def test_insert_at_negative_index(self):
        '''
            Tests invalid(negative) index raises error.
        '''
        self.assertRaises(ValueError, self.linkedlist.insert_at_index, 4, -1)

    def test_insert_at_invalid_index(self):
        '''
            Tests invalid(out of bounds) index raises error.
        '''
        self.assertRaises(ValueError, self.linkedlist.insert_at_index, 4, 1)
