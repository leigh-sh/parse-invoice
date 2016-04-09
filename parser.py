import configuration as conf
from invoicenumber import InvoiceNumber
import glob


def convert_chars_line_to_boolean_vector(chars_line):
    """
    :param chars_line: a string consists of 27 chars, each can be '|', '_' or ' ', plus '\n' as the last character
    :return: a vector array with 27 boolean values, representing an invoice number
    """
    boolean_vector = []
    chars_array = list(chars_line.rstrip('\n'))
    for char in chars_array:
        if char not in [' ', '|', '_']:
            raise Exception("Invalid character %s" % char)
        boolean_vector.append(char != ' ')
    return boolean_vector


def parse_invoice_numbers(file_name):
    segment_vector_array = []
    invoice_numbers = []
    file_lines = open(file_name, 'rb').read().splitlines()

    for line in file_lines:
        if len(line) % conf.digit_size != 0:
            raise Exception("Line's length must be a multiple of %s" % conf.digit_size)
        if line:
            row_boolean_vector = convert_chars_line_to_boolean_vector(line)
            segment_vector_array.append(row_boolean_vector)
        else:
            if len(segment_vector_array) != conf.digit_size:
                raise

            invoice_numbers.append(InvoiceNumber(segment_vector_array).get_value())
            segment_vector_array = []
    return invoice_numbers


# This function creates the output file
def create_output_file(invoice_numbers, output_file_name):
    with open(output_file_name, 'w') as outfile:
        for line in invoice_numbers:
            outfile.write(line + '\n')


if __name__ == "__main__":
    parsed_numbers = parse_invoice_numbers("")
    create_output_file(parsed_numbers, "")
