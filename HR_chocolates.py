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