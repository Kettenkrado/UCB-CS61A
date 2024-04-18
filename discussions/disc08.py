from Link import *

def strange_loop():
    """Return a Link s for which s.rest.first.rest is s.

    >>> s = strange_loop()
    >>> s.rest.first.rest is s
    True
    """
    s = Link(0)
    s.first, s.rest = s, s
    return s

def sum_rec(s):
    """
    Returns the sum of the elements in s.

    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_rec(a)
    14
    >>> sum_rec(Link.empty)
    0
    """
    # Use a recursive call to sum_rec
    if s is Link.empty:
        return 0
    else:
        return s.first + sum_rec(s.rest)

def sum_iter(s):
    """
    Returns the sum of the elements in s.

    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_iter(a)
    14
    >>> sum_iter(Link.empty)
    0
    """
    # Don't call sum_rec or sum_iter
    result = 0
    while s is not Link.empty:
        result += s.first
        s = s.rest
    return result

def overlap(s, t):
    """For increasing s and t, count the numbers that appear in both.

    >>> a = Link(3, Link(4, Link(6, Link(7, Link(9, Link(10))))))
    >>> b = Link(1, Link(3, Link(5, Link(7, Link(8)))))
    >>> overlap(a, b)  # 3 and 7
    2
    >>> overlap(a.rest, b)  # just 7
    1
    >>> overlap(Link(0, a), Link(0, b))
    3
    """
    if s == Link.empty or t == Link.empty:
        return 0

    if s.first < t.first:
        return overlap(s.rest, t)
    elif s.first > t.first:
        return overlap(s, t.rest)
    else:
        return 1 + overlap(s.rest, t.rest)

def divide(n, d):
    """Return a linked list with a cycle containing the digits of n/d.

    >>> display(divide(5, 6))
    0.8333333333...
    >>> display(divide(2, 7))
    0.2857142857...
    >>> display(divide(1, 2500))
    0.0004000000...
    >>> display(divide(3, 11))
    0.2727272727...
    >>> display(divide(3, 99))
    0.0303030303...
    >>> display(divide(2, 31), 50)
    0.06451612903225806451612903225806451612903225806451...
    """
    assert n > 0 and n < d
    result = Link(0)  # The zero before the decimal point
    remaining = result
    dividends = {}
    pos = 1
    n = n * 10

    while n not in dividends and n != 0:
        # 循环中断条件：n已经出现过了（无限循环开始），或者除尽
        dividends[n] = pos
        remaining.rest = Link(n // d)
        remaining = remaining.rest
        n = n % d * 10
        pos += 1
    
    if n == 0:
        # 除得尽特殊处理？否则该怎么做
        # 哦，懂了，前面的0不需要用pos记录，因为每次进入词典的n都乘十了
        # 词典里面存下第一次重复位置即可
        # 即cache[n] = tail, dividends[n] = remaining
        # 0.000400000000...的循环节实际上是0，把4看成特殊情况了，实际上还是一样的问题
        # 之前在组合数学中学过
        remaining.rest = Link(0)
        beginning = remaining.rest
        remaining = remaining.rest
        remaining.rest = beginning
        return result
        
    cycle_pos = result
    # 定位循环节
    for _ in range(dividends[n]):
        cycle_pos = cycle_pos.rest 
    remaining.rest = cycle_pos

    return result

    """
    cache = {}
    tail = result
    while n not in cache:
        q, r = 10 * n // d, 10 * n % d
        tail.rest = Link(q)
        tail = tail.rest
        cache[n] = tail
        n = r
    tail.rest = cache[n]
    return result
    """

def display(s, k=10):
    """Print the first k digits of infinite linked list s as a decimal.

    >>> s = Link(0, Link(8, Link(3)))
    >>> s.rest.rest.rest = s.rest.rest
    >>> display(s)
    0.8333333333...
    """
    assert s.first == 0, f'{s.first} is not 0'
    digits = f'{s.first}.'
    s = s.rest
    for _ in range(k):
        assert s.first >= 0 and s.first < 10, f'{s.first} is not a digit'
        digits += str(s.first)
        s = s.rest
    print(digits + '...')