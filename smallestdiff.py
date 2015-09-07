"""Given two lists, find the smallest difference between any two nums.

For example, given the lists:

  {10, 20, 14, 16, 18}
  {30, 23, 54, 33, 96}

The result would be 3, since 23-20=3 is the smallest difference of any
pair of numbers in those lists.

IMPORTANT: you must solve this with an algorithm that is faster than
O(ab) -- that is, you cannot compare each item of list a against
each item of list b (that would be O(ab) time).

Joel Burton <joel@joelburton.com>.

Adapted from a problem in `Cracking the Coding Interview, 6th Edition`.
Gayle Laakmann McDowell, Career Cup (Palo Alto, CA). 2015.
"""


# if smallest diff out of all nums in both lists
def smallest_diff(a, b):
    """Return smallest diff between all items in a and b.

        >>> smallest_diff([10, 20, 30, 40], [15, 25, 33, 45])
        3

        >>> smallest_diff([10, 12, 23, 12], [11, 23, 15, 42, 43])
        0
    """

    a.extend(b)
    a.sort()
    min_diff = abs(a[0] - a[1])
    for i in range(len(a)-1):
        diff = abs(a[i] - a[i+1])
        if diff < min_diff:
            min_diff = diff
    return min_diff


# if finding smallest diff when comparing nums in the two lists against each other
def smallest_diff(a, b):
    """Return smallest diff between all items in a and b.

        >>> smallest_diff([10, 20, 30, 40], [15, 25, 33, 45])
        3

        >>> smallest_diff([10, 12, 23, 12], [11, 23, 15, 42, 43])
        1
    """

       


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE WORK!\n"
