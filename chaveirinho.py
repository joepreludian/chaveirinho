import argparse
import ucompactor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input file to process', type=str)
    parser.add_argument('--output', help='output file to be compressed', type=str)
    parser.add_argument('--decompress', action='store_true')
    arguments = parser.parse_args()

    if arguments.decompress:
        ucompactor.decompress(input_file=arguments.input, output_file=arguments.output)
    else:
        ucompactor.compress(input_file=arguments.input, output_file=arguments.output)

if __name__ == '__main__':
    main()