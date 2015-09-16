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


def factorial(n):
    total = 1
    for num in range(1, n+1):
        total *= num
    print total

n = input()
factorial(n)


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