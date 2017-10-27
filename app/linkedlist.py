'''
    LinkedList implementation
'''
from app.node import Node

class LinkedList(object):
    '''
        Class implementing Linked List
    '''
    head = None
    _count = 0

    def insert_sorted(self, val):
        '''
            Inserts val -- sorted in descending order
            Args:
                self (LinkedList): Pointer to class object
                val (int): Integer value that needs to be inserted
        '''
        node = Node(val)
        if not self.head:
            self.head = node
        else:
            curr_node = self.head
            while val > curr_node.data and curr_node.next_node:
                prev_node = curr_node
                curr_node = curr_node.next_node
            if  curr_node == self.head and curr_node.data > val:
                node.next_node = curr_node
                curr_node = node
                self.head = node
            elif not curr_node.next_node and curr_node.data < val:
                curr_node.next_node = node
            else:
                node.next_node = curr_node
                prev_node.next_node = node
        self._count += 1

    def get_node_count(self):
        '''
            Returns _count of elements in the list
            Args:
                self (LinkedList): Pointer to class object
        '''
        return self._count

    def _get_element_at_index(self, index):
        '''
            Returns element at the given index in list
            Args:
                self (LinkedList): Pointer to class object
                index (int): Index for the element (Note: index starts at 0)
        '''
        curr_node = None
        if index <= self._count:
            curr_index = 0
            curr_node = self.head
            while curr_index < index:
                curr_node = curr_node.next_node
                curr_index += 1
        return curr_node

    def get_value_at_index(self, index):
        '''
            Returns Value at the given index in list
            Args:
                self (LinkedList): Pointer to class object
                index (int): Index for the element (Note: index starts at 0)
        '''
        return self._get_element_at_index(index).data
