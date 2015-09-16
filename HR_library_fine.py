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