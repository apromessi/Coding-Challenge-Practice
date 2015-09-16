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