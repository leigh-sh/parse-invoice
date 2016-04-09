from digit import Digit
import configuration as conf


class InvoiceNumber(object):
    """Return a new InvoiceNumber object."""

    def __init__(self, invoice_matrix):
        self.is_illegal = False
        self.digits = self._split_to_digits(invoice_matrix)
        self.value = self.to_string()

    def to_string(self):
        value = ''.join([digit.get_digit() for digit in self.digits])
        if self.is_illegal:
            value += ' ILLEGAL'
        return value

    def _split_to_digits(self, invoice_matrix):
        digits = []
        digit_vector = tuple()
        for i in range(0, conf.chars_in_line, conf.digit_size):
            for j in range(conf.digit_size):
                digit_vector += (tuple(invoice_matrix[j][i:i+conf.digit_size]))
            digit = Digit(digit_vector)
            digits.append(digit)
            if digit.get_digit() == '?':
                self.is_illegal = True
            digit_vector = tuple()
        return digits

    def get_value(self):
        return self.value