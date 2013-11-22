# encoding: utf8

from ucompactor.file import get_file, write_file, make_file_content
from ucompactor.huffmann import get_frequency, sort_frequency,\
    create_tree, create_table, compress_data_huffmann
from bwt import bwt_encoder, bwt_decoder
from ucompactor.rle import compress_rle


def compress(input_file, output_file):

    header = {'table': [], 'bwt': 0}

    raw_file = get_file(input_file)
    frequency_get = get_frequency(raw_file)
    sorted_frequency = sort_frequency(frequency_get)
    huffman_tree = create_tree(sorted_frequency)

    header['table'] = create_table(huffman_tree)

    body = compress_data_huffmann(raw_file, header['table'])

    encoder = bwt_encoder()
    header['bwt'], body = encoder.encode(body)

    body = compress_rle(body)

    output_file_data = make_file_content(header, body)

    try:
        write_file(output_file, output_file_data)
        print 'Arquivo comprimido!'
    except:
        print 'Ocorreu um erro ao comprimir o arquivo'


def decompress(input_file, output_file):
    print 'Ainda não implementado. =)' % (input_file, output_file)