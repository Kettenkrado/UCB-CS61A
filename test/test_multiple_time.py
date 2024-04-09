import time

def not_relatively_prime(a, b):
    """Return False if a and b are relatively prime,
    otherwise, return the smallest common factor that is larger than one of them
    
    >>> not_relatively_prime(5, 7)
    False
    >>> not_relatively_prime(12, 24)
    2
    """
    i = 2
    while i <= a and i <= b:
        if a % i == 0 and b % i == 0:
            return i
        i += 1
    return False


def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    result = a * b
    factor = 1
    while(factor):
        result, a, b = result // factor, a // factor, b // factor
        factor = not_relatively_prime(a, b)
    return result

time_start = time.time()  # 记录开始时间
multiple(8158, 9672) # function()   执行的程序
time_end = time.time()  # 记录结束时间
time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
print(time_sum)