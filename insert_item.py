# given a array, how do you move a character in one location and
# place it at the other location?

def insert(mylist, orig_index, new_index):
    """
    >>> insert([1, 2, 3, 4, 5, 6, 7], 1, 4)
    [1, 3, 4, 5, 2, 6, 7]

    >>> insert([1, 2, 3, 4, 5, 6, 7], 4, 1)
    [1, 5, 2, 3, 4, 6, 7]
    """

    char = mylist[orig_index]
    if orig_index < new_index:
        for i in range(orig_index, new_index):
            mylist[i] = mylist[i + 1]
        mylist[new_index] = char
    if orig_index > new_index:
        for i in range(orig_index, new_index, -1):
            mylist[i] = mylist[i - 1]
        mylist[new_index] = char
    return mylist

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
