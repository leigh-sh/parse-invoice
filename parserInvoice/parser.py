import sys
import getopt

import configuration as conf
from invoicenumber import InvoiceNumber


def convert_chars_line_to_boolean_vector(chars_line):
    """
    :param chars_line: a string consists of 27 chars, each can be '|', '_' or ' ', plus '\n' as the last character
    :return: a vector array with 27 boolean values, representing an invoice number
    """
    if not chars_line:
        raise Exception("invalid line")
    boolean_vector = []
    chars_array = list(chars_line.rstrip('\n'))
    if len(chars_array) != conf.chars_in_line:
        raise Exception("line's length %s is invalid, it should be 27" % len(chars_array))
    for char in chars_array:
        if char not in [' ', '|', '_']:
            raise Exception("Invalid character %s" % char)
        boolean_vector.append(char != ' ')
    return boolean_vector


def parse_invoice_numbers(file_lines):
    """
    :param file_lines: a matrix of size 27x4n where n is the number of invoices.
    :return: a matrix of strings, in length of n. Each string is an invoice number of 9 digits.
    """
    segment_vector_array = []
    invoice_numbers = []

    for line in file_lines:
        if line:
            line = line.rstrip('\n')
            if len(line) != 27:
                raise Exception("Line's length must be  %s" % str(conf.digit_size))
            boolean_vector = convert_chars_line_to_boolean_vector(line)
            segment_vector_array.append(boolean_vector)
        else:
            if len(segment_vector_array) != conf.digit_size:
                raise Exception("Invalid format of invoice number lines")

            invoice_numbers.append(InvoiceNumber(segment_vector_array).get_value())
            segment_vector_array = []
    return invoice_numbers


def create_output_file(invoice_numbers, output_file_name):
    """
    :param invoice_numbers: a matrix of strings, each is an invoice number of 9 digits.
    :param output_file_name: the desired name for the output file that will consist the invoice numbers matrix.
    :return:
    """
    with open(output_file_name, 'w') as outfile:
        for line in invoice_numbers:
            outfile.write(line + '\n')


def read_input_file(file_name):
    """
    :param file_name: the name of the input file.
    :return: a matrix of size 27x4n where n is the number of invoices.
    """
    return open(file_name, 'rb').read().splitlines()


def main(argv):
    input_file = ''
    output_file = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'parser.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'parser.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
    input_matrix = read_input_file(input_file)
    parsed_numbers = parse_invoice_numbers(input_matrix)
    create_output_file(parsed_numbers, output_file)

if __name__ == "__main__":
    main(sys.argv[1:])
