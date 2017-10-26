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
        if data:
            if isinstance(data, data_type):
                self.data = data
            else:
                raise ValueError
        if next_node:
            if isinstance(next_node, node_type):
                self.next_node = next_node
            else:
                raise ValueError


    def __str__(self):
        return str(self.data)

if __name__ == '__main__':
    node = Node(1, None)
    print node
