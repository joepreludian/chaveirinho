from ucompactor.huffmann import get_file, get_frequency, sort_frequency, create_tree, create_table


def compress(input_file, output_file):

    raw_file = get_file(input_file)
    frequency_get = get_frequency(raw_file)
    sorted_frequency = sort_frequency(frequency_get)
    huffmann_tree = create_tree(sorted_frequency)

    huffmann_table = create_table(huffmann_tree)

    print 'comprimindo arquivo %s em %s' % (input_file, output_file)


def decompress(input_file, output_file):
    print 'descomprimindo arquivo %s em %s' % (input_file, output_file)