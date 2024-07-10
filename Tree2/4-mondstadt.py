inp = input("Enter Input : ").split('/')
p = list(map(int, inp[0].split()))
sum = 0
for e in p:
    sum += e
print(sum)
n = len(p)
inp[1] = inp[1].split(',')
for i in inp[1]:
    kn = list(map(int, i.split()))
    sum1 = p[kn[0]]
    sum2 = p[kn[1]]
    if kn[0]*2+1 < n:
        sum1 += p[kn[0]*2+1]
    if kn[0]*2+2 < n:
        sum1 += p[kn[0]*2+2]

    if kn[1]*2+1 < n:
        sum2 += p[kn[1]*2+1]
    if kn[1]*2+2 < n:
        sum2 += p[kn[1]*2+2]
    print(kn[0], end='')
    if sum1 == sum2:
        print('=', end='')
    elif sum1 < sum2:
        print('<', end='')
    elif sum1 > sum2:
        print('>', end='')
    print(kn[1], end='')
    print()
