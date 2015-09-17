def sort_ab(a, b):
    """Given already-sorted lists, `a` and `b`, return sorted list of both.

    You may not use sorted() or .sort().

    Check edge cases of empty lists:

        >>> sort_ab([], [])
        []

        >>> sort_ab([1, 2,3], [])
        [1, 2, 3]

        >>> sort_ab([], [1, 2, 3])
        [1, 2, 3]

    Check:

        >>> sort_ab([1, 3, 5, 7, 8, 11], [2, 6, 8, 10])
        [1, 2, 3, 5, 6, 7, 8, 8, 10, 11]
    """

    ab = []
    if a and b:
        a_i = 0
        b_i = 0
        while a_i < len(a) and b_i < len(b):
            if a[a_i] < b[b_i]:
                ab.append(a[a_i])
                a_i += 1
            elif a[a_i] >= b[b_i]:
                ab.append(b[b_i])
                b_i += 1
        a = a[a_i:]
        b = b[b_i:]

    if a:
        ab.extend(a)
    if b:
        ab.extend(b)
    return ab


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE A MERGE CHAMPION!!\n"
