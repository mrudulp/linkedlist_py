'''
    This contains declaration for Node class
'''
class Node(object):
    '''
        Node class. Holds integer data and pointer to next Node if available
    '''
    data = None
    next_node = None
    def __init__(self, data=None, next_node=None):

        if data:
            if isinstance(data, int):
                self.data = data
            else:
                raise ValueError("Data arguments should be of type<int>")
        if next_node:
            if isinstance(next_node, Node):
                self.next_node = next_node
            else:
                raise ValueError("Node argument should be of type<Node>")

    def __str__(self):
        return str(self.data)
