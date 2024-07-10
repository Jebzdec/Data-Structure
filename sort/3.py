def insertionsort(x, ls=[], i=0,):
    if i >= len(ls) or x[0] < ls[i]:
        ls.insert(i, x[0])
        if (len(ls) > 1):
            print(f'insert {x[0]} at index {i} : {ls} ', end='')
        x.pop(0)
        if len(x) > 0 and len(ls) > 1:
            print(x)
        if len(x) > 0:
            insertionsort(x, ls, 0)
    else:
        insertionsort(x, ls, i+1)

    return ls


inp = list(map(int, input("Enter Input : ").split()))
lst = []
lst = insertionsort(inp)
print('\nsorted')
print(lst)
