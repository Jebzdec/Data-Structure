def asteroid_collision(asts, n):
    if n <= 0:
        return 'asts'
    if asts[n] < 0 and asts[n-1] > 0:
        if (asts[n]*-1 > asts[n-1]):
            asts.pop(n-1)
        elif (asts[n]*-1 < asts[n-1]):
            asts.pop(n)
        elif (asts[n]*-1 == asts[n-1]):
            asts.pop(n-1)
            asts.pop(n-1)
        return asteroid_collision(asts, len(asts)-1)
    return asteroid_collision(asts, n-1)


x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(x, len(x)-1))
