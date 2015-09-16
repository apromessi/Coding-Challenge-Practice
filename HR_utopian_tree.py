def calculate_growth(cycles):
    height = 1
    for n in range(1, cycles + 1):
        if n % 2 != 0:
            height *= 2
        else:
            height += 1
    print height

tests = int(raw_input())
for t in range(tests):
    cycles = int(raw_input())
    calculate_growth(cycles)
