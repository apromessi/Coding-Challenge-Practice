

def Descending_Order(num):
    """Your task is to make a function that can take any non-negative integer
    as a argument and return it with it's digits in descending order.
    Descending order means that you take the highest digit and place the next
    highest digit immediately after it.

    >>>Descending_Order(0)
    0

    >>>Descending_Order(15)
    51

    >>>Descending_Order(123456789)
    987654321

    """

    num_str = str(num)
    num_list = []
    for num in num_str:
        num_list.append(num)
    num_list.sort()
    num_sorted = ""
    for num in num_list[::-1]:
        num_sorted += num
    return int(num_sorted)

##########################################


def pattern(n):
    nums = ""
    if n > 0:
        for i in range(n):
            nums += str((i+1) % 10)
        for i in range(n):
            print (" " * (n-i)) + nums


def complete_the_pattern(n):
    if n < 1:
        return ""
    else:
        to_print = "1"
        for i in range(2, n+1):
            to_print += "\n" + (str(i) * i)
        return to_print


def title_case(title, minor_words=None):
    """
    >>>title_case('a clash of KINGS', 'a an the of')
    'A Clash of Kings'

    >>>title_case('THE WIND IN THE WILLOWS', 'The In')
    'The Wind in the Willows'

    >>>title_case('the quick brown fox')
    'The Quick Brown Fox'
    """

    title_words = title.split()
    title_to_print = ""

    if minor_words:
        minor_words_set = set(minor_words.split())
        print minor_words_set
        for word in minor_words_set:
            minor_words_set.remove(word)
            minor_words_set.add(word.lower())
        print minor_words_set

    if len(title) > 1:
        title_to_print += title_words[0].capitalize()
        for word in title_words[1:]:
            if word.lower() in minor_words_set:
                title_to_print += " " + word.lower()
            else:
                title_to_print += " " + word.capitalize()

    return title_to_print
