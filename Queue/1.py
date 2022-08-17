q = []
deq = []


def func(key, value):
    global q
    global deq
    if key == 'E':
        q.append(value)
    elif key == 'D':
        if q:
            deq.append(q[0])
            print(f'{q[0]} <- ', end='')
        q = q[1:]
        if value:
            q.append(value)

    Print(q)
    print()


def Print(a):
    if a:
        print(*a, sep=', ', end='')
    else:
        print('Empty', end='')


Input = input("Enter Input : ").split(',')
for i in Input:
    try:
        k, v = i.split()
        func(k, int(v))
    except:
        func(i, None)

Print(deq)
print(' : ', sep=', ', end='')
Print(q)
