def fizz_buzz(n):
    for num in xrange(1, n+1):
        to_print = ''
        if num % 3 == 0:
            to_print += "Fizz"
        if num % 5 == 0:
            to_print += "Buzz"
        if to_print == '':
            to_print = str(num)
    return to_print
