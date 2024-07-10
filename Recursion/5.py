def staircase(n, m):

    if inp == 0:
        print('Not Draw!')
        return
    elif inp > 0:
        if n >= inp:
            return
        print('_' if m < inp-n-1 else '#', end='')
        if m+1 == inp:
            print()
            staircase(n+1, 0)
        else:
            staircase(n, m+1)

    else:
        if n >= inp*-1:
            return
        print('_' if m < n else '#', end='')
        if m+1 == inp*-1:
            print()
            staircase(n+1, 0)
        else:
            staircase(n, m+1)


inp = int(input("Enter Input : "))
staircase(0, 0)
