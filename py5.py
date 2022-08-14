print("*** Minesweeper ***")
print("Enter input(5x5) : ", end='')
ip = input().split(',')
k = 0
for i in range(5):
    print("[", end='')
    for j in range(5):
        print("\'%s\'" % (ip[k]), end='')
        if k % 5 != 4:
            print(",", end='')
        k += 1

    print("]")
