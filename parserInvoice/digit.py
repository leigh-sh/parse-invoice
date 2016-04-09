class Digit(object):
    bit_vector_to_digit = {
        (False, True, False, True, False, True, True, True, True): '0',
        (False, False, False, False, False, True, False, False, True): '1',
        (False, True, False, False, True, True, True, True, False): '2',
        (False, True, False, False, True, True, False, True, True): '3',
        (False, False, False, True, True, True, False, False, True): '4',
        (False, True, False, True, True, False, False, True, True): '5',
        (False, True, False, True, True, False, True, True, True): '6',
        (False, True, False, False, False, True, False, False, True): '7',
        (False, True, False, True, True, True, True, True, True): '8',
        (False, True, False, True, True, True, False, True, True): '9'
    }

    """Return a new Digit object."""
    def __init__(self, digit_vector):
        self.value = self.parse_digit(digit_vector)

    def get_digit(self):
        """ 
        :return: the digit's value which is a string.
        """
        return self.value

    def parse_digit(self, digit_vector):
        """ 
        :param digit_vector: a boolean vector in length 9 that represents the digit
        :return: the digit's value, if exists, '?' otherwise.
        """
        return self.bit_vector_to_digit.get(digit_vector) or '?'
