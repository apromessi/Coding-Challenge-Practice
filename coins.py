"""Calculate possible change from combinations of dimes and pennies.

Given an infinite supply of dimes and pennies, find the different
amounts of change can be created with exact `num_coins` coins?

For example, when num_coins = 3, you can create:

    3 = penny + penny + penny
   12 = dime + penny + penny
   21 = dime + dime + penny
   30 = dime + dime + dime
"""

DIME = 10
PENNY = 1


def coins(num_coins):
    """Find change from combinations of k length of dimes and pennies.

    This should return a set of the unique amounts of change possible.

        >>> coins(0) == {0}
        True

        >>> coins(1) == {1, 10}
        True

        >>> coins(2) == {2, 11, 20}
        True

        >>> coins(3) == {3, 12, 21, 30}
        True

        >>> coins(4) == {4, 13, 22, 31, 40}
        True

        >>> coins(10) == {10, 19, 28, 37, 46, 55, 64, 73, 82, 91, 100}
        True
    """

    totals = set([])
    total = num_coins
    totals.add(total)

    for i in range(num_coins):
        total += 10
        total -= 1
        totals.add(total)

    return totals


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU CAN TAKE THAT TO THE BANK!\n"
