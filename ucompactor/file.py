def get_file(input_file):

    f = open(input_file, 'rb')
    try:
        raw_file = f.read()

    finally:
        f.close()

    return raw_file


def write_file(output_file, data):

    f = open(output_file, 'w')
    try:
        f.write(data)
    finally:
        f.close()

    return True


def make_file_content(header, body):

    data_output = "%s" % header['bwt']

    for item in header['table']:
        data_output += '%s%s' % (item[0], item[1])

    data_output += ':%s' % body

    return data_output