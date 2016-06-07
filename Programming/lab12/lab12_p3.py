class Fraction(object):
    def __init__(self, numerator, denominator):
        """Inits Fraction with values numerator and denominator. """

        self.__numerator = numerator
        self.__denominator = denominator
        self.reduce()

    def copy(self):
        """Creates a copy of a given Fraction."""

        return Fraction(self.__numerator, self.__denominator)

    def __repr__(self):
        """Returns Fraction value as x/y. """

        return str(self.__numerator) + '/' + str(self.__denominator)

    def getNumerator(self):
        """Returns the numerator of a Fraction."""

        return self.__numerator

    def getDenominator(self):
        """Returns the denominator of a Fraction."""

        return self.__denominator

    def setNumerator(self, value):
        """Sets the numerator of a Fraction to the provided value."""

        self.__numerator = value

    def setDenominator(self, value):
        """ Sets the denominator of a Fraction to the provided value.

            Raises a ValueError exception if a value of zero provided.
        """
        if value == 0:
            raise ValueError('Divide by Zero Error')

        self.__denominator = value

    def adjust(self, factor):
        """ Multiplies numerator and denominator by a factor. """
        self.__numerator *= factor
        self.__denominator *= factor

    def reduce(self):
        """ Reduces self to simplest terms. Also removes the signs
            if both numerator and denominator are negative. """

        if self.__numerator < 0 and self.__denominator < 0:
            self.__adjust(-1)

        divisor = find_gcd(self.__numerator, self.__denominator)
        self.__numerator = int(self.__numerator/divisor)
        self.__denominator = int(self.__denominator/divisor)

def find_gcd(numer, denom):
    """ Finds greatest common divisor of the fraction's elements. """
    if denom ==0:
        return numer
    return find_gcd(denom, numer%denom)
