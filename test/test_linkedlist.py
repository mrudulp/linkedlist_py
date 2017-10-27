'''
    Tests to test Linked List class
'''

import unittest

from app.linkedlist import LinkedList

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

    def test_insert_sorted_head(self):
        '''
            Tests element is inserted [at head] in sorted(ascending) order
        '''
        self.linkedlist.insert_sorted(4)
        self.assertEqual(self.linkedlist.get_node_count(), 1)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.linkedlist.insert_sorted(3)
        self.assertEqual(self.linkedlist.get_node_count(), 2)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 3)
        self.assertEqual(self.linkedlist.get_value_at_index(1), 4)

    def test_insert_sorted_tail(self):
        '''
            Tests element is inserted [at tail] in sorted(ascending) order
        '''
        self.linkedlist.insert_sorted(4)
        self.assertEqual(self.linkedlist.get_node_count(), 1)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.linkedlist.insert_sorted(5)
        self.assertEqual(self.linkedlist.get_node_count(), 2)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.assertEqual(self.linkedlist.get_value_at_index(1), 5)

    def test_insert_sorted_middle(self):
        '''
            Tests elements are inserted [somewhere between 2 nodes] in sorted(ascending) order
        '''
        self.linkedlist.insert_sorted(4)
        self.assertEqual(self.linkedlist.get_node_count(), 1)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.linkedlist.insert_sorted(6)
        self.assertEqual(self.linkedlist.get_node_count(), 2)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.assertEqual(self.linkedlist.get_value_at_index(1), 6)
        self.linkedlist.insert_sorted(5)
        self.assertEqual(self.linkedlist.get_node_count(), 3)
        self.assertEqual(self.linkedlist.get_value_at_index(0), 4)
        self.assertEqual(self.linkedlist.get_value_at_index(1), 5)
        self.assertEqual(self.linkedlist.get_value_at_index(2), 6)

    def test_rejects_non_integer_value(self):
        '''
            Tests non integer value is rejected and an error is raised
        '''
        self.assertRaises(ValueError, self.linkedlist.insert_sorted, "4")
        self.assertRaises(ValueError, self.linkedlist.insert_sorted, 1.5)
