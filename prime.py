limit = int(input('upper limit?\n'))
for n in range(2, limit):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(n, end=", ")
