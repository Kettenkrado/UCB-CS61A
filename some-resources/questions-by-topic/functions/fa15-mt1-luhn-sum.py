# fa15
def luhn_sum(n):
    """Return the Luhn sum of n.
    
    >>> luhn_sum(135)     # 1 + 6 + 5
    12
    >>> luhn_sum(185)     # 1 + (1+6) + 5
    13
    >>> luhn_sum(138743)  # From lecture: 2 + 3 + (1+6) + 7 + 8 + 3
    30
    """
    def luhn_digit(digit):
        x = digit * multiplier
        return (x // 10) + x % 10
    total, multiplier = 0, 1
    while n:
        n, last = n // 10, n % 10
        total = total + luhn_digit(last)
        multiplier = 3 - multiplier
    return total