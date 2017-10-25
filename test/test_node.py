'''
    Contains Tests for Node class
'''
import unittest

from app.node import Node

class TestNode(unittest.TestCase):
    '''
        Tests to verify Node class & its data types
    '''

    def test_empty_data_next_node(self):
        '''
            Verify None as data & next_node is accepted and Node object is created
        '''
        node = Node()
        self.assertIsInstance(node, Node)

    def test_accepts_integer_as_data(self):
        '''
            Verify integer as data is accepted and Node object is created
        '''
        node = Node()
        self.assertIsInstance(node, Node)

    def test_rejects_string_as_data(self):
        '''
            Verify string as data is rejected and error is raised
        '''
        self.assertRaises(ValueError, Node, "data")

    def test_rejects_float_as_data(self):
        '''
            Verify float as data is rejected and error is raised
        '''
        self.assertRaises(ValueError, Node, 1.0)

    def test_rejects_string_as_next_node(self):
        '''
            Verify String or Non Node instance is rejected and error is raised
        '''
        self.assertRaises(ValueError, Node, 1, "data")
