# different ways of finding the nth fibonacci term
# [1, 1, 2, 3, 5, 8, 13, 21]


def fib(n):
    """
    >>> fib(5)
    5

    >>> fib(1)
    1

    >>> fib(8)
    21

    """

    if n <= 2:
        return 1
    else:
        a, b = 1, 1
        n = n - 2
        while n:
            a, b = b, a+b
            n -= 1
        return b


def fib_recursive(n):
    """
    >>> fib_recursive(5)
    5

    >>> fib_recursive(1)
    1

    >>> fib_recursive(8)
    21

    """
    if n <= 2:
        return 1
    num = fib(n-1) + fib(n-2)
    return num


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE WORK!\n"
