def diagonal_diff(n, matrix):
    diagonal_1 = 0
    diagonal_2 = 0
    for i in range(n):
        diagonal_1 += int(matrix[i][i])
        diagonal_2 += int(matrix[n-i-1][i])
    diff = abs(diagonal_1 - diagonal_2)
    return diff

n = input()
matrix = []
for num in range(n):
    matrix.append(raw_input().split())

print diagonal_diff(n, matrix)


def counts(n, array):
    positives = 0
    negatives = 0
    zeros = 0
    for num in array:
        num = float(num)
        if num == 0:
            zeros += 1
        elif num > 0:
            positives += 1
        else:
            negatives += 1
    print positives/float(n)
    print negatives/float(n)
    print zeros/float(n)

n = input()
array = raw_input().split()

counts(n, array)


def stairs(n):
    for i in range(1, n+1):
        print " " * (n-i) + "#" * i

n = input()
stairs(n)


def time_converter(time_in):
    time = time_in.split(":")
    if time[2][2:] == "PM" and int(time[0]) < 12:
        hours = int(time[0]) + 12
        if hours < 24:
            time[0] = str(hours)
    if time[2][2:] == "AM" and int(time[0]) == 12:
        time[0] = "00"
    time[2] = time[2][:2]
    time_out = ":".join(time)
    print time_out

time_in = raw_input()
time_converter(time_in)


def library_fine(returned, expected):
    fine = 0
    years = returned[2] - expected[2]
    months = returned[1] - expected[1]
    days = returned[0] - expected[0]

    if years > 0:
        fine = 10000
    elif years == 0 and months > 0:
        fine = months * 500
    elif years == 0 and months == 0 and days > 0:
        fine = days * 15
    print fine

returned = raw_input().split()
for i in range(len(returned)):
    x = returned.pop(0)
    returned.append(int(x))
expected = raw_input().split()
for i in range(len(expected)):
    x = expected.pop(0)
    expected.append(int(x))

library_fine(returned, expected)


def factorial(n):
    total = 1
    for num in range(1, n+1):
        total *= num
    print total

n = input()
factorial(n)


def prof(n_k, students):
    k = int(n_k[1])
    students.sort()
    early_count = 0
    for student in students:
        student = int(student)
        if student <= 0:
            early_count += 1
        if early_count >= k:
            return "NO"
    if early_count < k:
        return "YES"

t = input()
for i in range(t):
    n_k = raw_input().split()
    students = raw_input().split()
    print prof(n_k, students)

T = int(raw_input())
for i in range(0, T):
    funds, choc, wrappers_per_choc = [int(x) for x in raw_input().split(' ')]
    chocolates = funds/choc
    wrappers = chocolates
    while wrappers >= wrappers_per_choc:
        free_chocs = wrappers/wrappers_per_choc
        chocolates += free_chocs
        wrappers -= free_chocs * wrappers_per_choc
        wrappers += free_chocs
    answer = chocolates

    print answer

def partition(ar):    
    left = []
    right = []
    pivot = ar[0]
    for num in ar[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    left.append(pivot)
    left.extend(right)

    print " ".join([str(x) for x in left])

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)


def max_toys(prices, rupees):
    spent = 0
    answer = 0
    prices.sort()
    for price in prices:
        if spent + price <= rupees:
            spent += price
            answer += 1
    return answer

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    prices = map(int, raw_input().split())
    print max_toys(prices, k)


def modified_fib(a, b, n):
    fib = [a, b]
    for i in range(2, n):
        next = fib[i-2] + (fib[i-1] ** 2)
        fib.append(next)
    print fib[-1]

a, b, n = raw_input().split()
modified_fib(int(a), int(b), int(n))


def happiness_calculator(array, a, b):
    happiness = 0
    for num in array:
        if num in a:
            happiness += 1
        elif num in b:
            happiness -= 1
    print happiness

n, m = raw_input().split()
array = raw_input().split()
a = set(raw_input().split())
b = set(raw_input().split())
happiness_calculator(array, a, b)


n = int(raw_input())
words = {}
words_order = []
for i in range(n):
    word = raw_input()
    words_order.append(word)
    words[word] = words.get(word, 0) + 1
print len(words)
printed = set([])
for word in words_order:
    if word not in printed:
        print words[word],
        printed.add(word)
    

# STRING DRILLS:

def swap_case(string):
    swapped_string = ""
    for char in string:
        if char.isupper():
            swapped_string += char.lower()
        elif char.islower():
            swapped_string += char.upper()
        else:
            swapped_string += char
    return swapped_string

string = raw_input()
print swap_case(string)


string = raw_input()
words = string.split()
joined = "-".join(words)
print joined


string = raw_input()
i, c = raw_input().split()
i = int(i)
print string[:i] + c + string[i+1:]