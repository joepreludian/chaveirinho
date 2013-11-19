import operator


def get_file(input_file):

    f = open(input_file, 'rb')
    try:
        raw_file = f.read()

    finally:
        f.close()

    return raw_file


def get_frequency(input_stream):

    frequency = {}

    for data in input_stream:
        if data in frequency:
            frequency[data] += 1
        else:
            frequency[data] = 1

    return frequency


def sort_frequency(frequency_dict):

    ordered_frequency = sorted(frequency_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    return ordered_frequency



class Node(object):
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data

        @param data node data object to insert
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        """
        Lookup node containing data

        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def delete(self, data):
        """
        Delete node containing data

        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()

    def tree_data(self):
        """
        Generator to get the tree nodes data
        """
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else: # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node.data
                node = node.right