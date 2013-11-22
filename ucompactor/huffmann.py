import Queue


def get_frequency(input_stream):

    frequencies = {}
    frequencies_total = 0

    for data in input_stream:
        if data in frequencies:
            frequencies[data] += 1
        else:
            frequencies[data] = float(1)

        frequencies_total += 1

    for letter in frequencies:
        frequencies[letter] = round((frequencies[letter]*100) / frequencies_total, 3)

    return frequencies


def sort_frequency(frequency_dict):

    ordered_frequency = sorted(frequency_dict.iteritems(), key=lambda freq: freq[1])
    return ordered_frequency


class HuffmanNode(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def create_tree(frequencies):
    p = Queue.Queue()

    for value in frequencies:
        p.put(value)

    while p.qsize() > 1:
        r,l = p.get(), p.get()
        node = HuffmanNode(l, r)
        p.put((node, l[1]+r[1]))

    return p.get()

_huffmann_table = []
def _iterate_table(huffmann_tree, direction=None, binary_path=''):

    node = huffmann_tree[0]

    if direction == 'left':
        binary_path += '1'
    elif direction == 'right':
        binary_path += '0'

    if isinstance(node, HuffmanNode):
        left, right = node.children()
        _iterate_table(left, direction='left', binary_path=binary_path)
        _iterate_table(right, direction='right', binary_path=binary_path)
    else:
        _huffmann_table.append((node[0], binary_path))


def create_table(huffmann_tree):

    _iterate_table(huffmann_tree)
    new_huffmann = _normalize_table(_huffmann_table)

    return new_huffmann


def _normalize_table(huffmann_table):

    size = 0
    new_table = []

    for item in huffmann_table:
        if len(item[1]) > size:
            size = len(item[1])

    for item in huffmann_table:
        new_table.append((item[0], item[1].zfill(size)))

    huffmann_table = new_table
    return huffmann_table


def compress_data_huffmann(raw_file, huffmann_table):

    return_file = raw_file

    for huffman_data in huffmann_table:
        return_file = return_file.replace(huffman_data[0], huffman_data[1])

    return return_file


