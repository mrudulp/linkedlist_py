'''
    LinkedList implementation
'''
from app.node import Node

class LinkedList(object):
    '''
        Class implementing Linked List
    '''
    head = None
    tail = None
    _count = 0

    # def __str__(self):
    #     if len(self.nodes):
    #         str_node = "["
    #         curr_node = self.nodes[0]
    #         while curr_node.next_node:
    #             str_node += "{0},".format(curr_node)
    #         str_node += "{0}".format(curr_node)
    #     else:
    #         return "Empty List"

    # def print_list(self, nodes):
    #     if len(nodes) == 1:
    #         return nodes[0].data
    #     else:
    #         return self.print_list(nodes[0].next_node)

    def append_to_list(self, val):
        '''
            Appends val as a new Node Element to the end of list
            Args:
                self (LinkedList): Pointer to class object
                val (int): Integer value that needs to be appended
        '''
        node = Node(val)
        if not self.tail:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_node = node
            self.tail = node
        self._count += 1

    def insert(self, val):
        '''
            Inserts val as a new Node Element to the start of the list
            Args:
                self (LinkedList): Pointer to class object
                val (int): Integer value that needs to be inserted
        '''
        node = Node(val)
        if not self.tail:
            self.head = node
            self.tail = self.head
        else:
            node.next_node = self.head
            self.head = node
        self._count += 1

    def insert_at_index(self, val, index):
        '''
            Inserts val as a new Node Element to the start of the list
            Args:
                self (LinkedList): Pointer to class object
                val (int): Integer value that needs to be inserted
                index (int): Index at which element needs to be inserted
        '''
        node = Node(val)
        if index == 0:
            self.insert(val)
        elif index == self._count:
            self.append_to_list(val)
        elif index > self._count or index < 0:
            raise ValueError("Bad Index")
        else:
            curr_node = self._get_element_at_index(index-1)
            node.next_node = curr_node.next_node
            curr_node.next_node = node
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
        if index <= self._count:
            curr_index = 0
            curr_node = self.head
            while curr_index < index:
                curr_node = curr_node.next_node
                curr_index += 1
            return curr_node
        else:
            return None

    def get_value_at_index(self, index):
        '''
            Returns Value at the given index in list
            Args:
                self (LinkedList): Pointer to class object
                index (int): Index for the element (Note: index starts at 0)
        '''
        return self._get_element_at_index(index).data

if __name__ == '__main__':
    linked_list = LinkedList()
    print linked_list
