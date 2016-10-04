# Module for various number tools


def is_palindrome(num):
    """ Check if a number is a palindrome """
    return str(num) == str(num)[::-1]


def divisors(num, proper=True):
    """
    Return the divisors of the number
    num should be greater than 1

    If proper is set to True, return the Proper divisors i.e all divisors
    except the number itself.
    """
    yield 1
    low_divisor = 2
    while low_divisor**2 <= num:
        if num % low_divisor == 0:
            high_divisor = int(num / low_divisor)
            yield low_divisor
            if low_divisor != high_divisor:
                yield high_divisor
        low_divisor += 1
    if not proper:
        yield num
