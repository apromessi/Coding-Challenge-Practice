def find_survivor(num_people, kill_every):
    """Given num_people in a circle, kill everyone [kill_every]th person, return survivor.

        >>> find_survivor(4, 2)
        1

        >>> find_survivor(41, 3)
        31

    As a sanity case, if never skip anyone, the last person will be our survivor:

        >>> find_survivor(10, 1)
        10
    """


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. W00T!\n"
