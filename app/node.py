'''
    This contains declaration for Node class
'''
class Node(object):
    '''
        Node class. Holds integer data and pointer to next Node if available
    '''
    def __init__(self, data=None, next_node=None):

        print "Data_{0}::Next_node::{1}".format(data, next_node)
        data_type = (int)
        node_type = (Node)
        if data or next_node:
            if isinstance(data, data_type) and isinstance(next_node, node_type):
                self.data = data
                self.next_node = next_node
            else:
                raise ValueError
