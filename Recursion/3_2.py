def permu(now, n):
    if n == 0:
        print(now)
        return
    permu(now+'0', n-1)
    permu(now+'1', n-1)


inp = int(input("Enter Number : "))
if inp < 0:
    print('!!')
elif inp == 0:
    print('0')
else:
    permu("", inp)
