def reverse_list(a_list):
    """
    >>> reverse_list(['a', 'b', 'c', 'd', 'e'])
    ['e', 'd', 'c', 'b', 'a']

    >>> reverse_list([5])
    [5]
    """
    for i in range(len(a_list)/2):
        temp = a_list[i]
        a_list[i] = a_list[-i-1]
        a_list[-i-1] = temp
    return a_list


def reverse_list_slicing(a_list):
    """
    >>> reverse_list(['a', 'b', 'c', 'd', 'e'])
    ['e', 'd', 'c', 'b', 'a']

    >>> reverse_list([5])
    [5]
    """
    return a_list[::-1]


def reverse_string(string):
    """
    >>> reverse_string('abcde')
    'edcba'

    >>> reverse_string('Hello World!')
    '!dlroW olleH'
    """

    pass

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"