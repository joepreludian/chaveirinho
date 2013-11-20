import operator, Queue
from ucompactor import exceptions as ex


def get_file(input_file):

    f = open(input_file, 'rb')
    try:
        raw_file = f.read()

    finally:
        f.close()

    return raw_file


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
        return (self.left, self.right)


def create_tree(frequencies):
    p = Queue.Queue()

    for value in frequencies:
        p.put(value)

    while p.qsize() > 1:
        r,l = p.get(), p.get()
        node = HuffmanNode(l, r)
        p.put((node, l[1]+r[1]))

    return p.get()


def create_table(huffmann_tree):
    pass