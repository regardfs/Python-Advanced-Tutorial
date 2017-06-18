# transfer n to binary mode

n = -37
bin(n)

# int.bit_length() Return the number of bits necessary to represent an integer in binary, excluding the sign and
# leading zeros. More precisely, if x is nonzero, then x.bit_length() is the unique positive integer k such that
# 2**(k-1) <= abs(x) < 2**k. Equivalently, when abs(x) is small enough to have a correctly rounded logarithm,
# then k = 1 + int(log(abs(x), 2)). If x is zero, then x.bit_length() returns 0.
n.bit_length()
# return 6


def bit_length(self):
    s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
    s = s.lstrip('-0b') # remove leading zeros and minus sign
    return len(s)       # len('100101') --> 6



