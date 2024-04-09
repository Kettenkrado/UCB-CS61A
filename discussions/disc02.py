def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    def print_all(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return print_all

def find_digit(k):
    """Returns a function that returns the kth digit of x.

    >>> find_digit(2)(3456)
    5
    >>> find_digit(2)(5678)
    7
    >>> find_digit(1)(10)
    0
    >>> find_digit(4)(789)
    0
    """
    assert k > 0
    def find_digit_in_number(n):
        i = 1
        while n != 0:
            if i == k:
                return n % 10
            n //= 10
            i += 1
        return 0
    return find_digit_in_number

    """
    Or: 
    assert k > 0
    return lambda x: (x // pow(10, k-1)) % 10
    """

def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        while x // (10 ** k) > 0:
            if x % (10 ** k) != x // (10 ** k) % (10 ** k):
                return False
            x //= (10 ** k) 
        return True
    return check
    """
            if (x % 10) != (x // (10 ** k)) % 10:
                return False
            x //= 10
    """