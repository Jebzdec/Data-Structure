inp = input('Enter Input : ').split('/')
inp[0] = int(inp[0])
inp[1] = list(map(int, inp[1].split()))
c = [0]*inp[0]
for j in range(len(inp[1])):
    idx = 0
    Min = c[0]
    for i in range(len(c)):
        if c[i] < Min:
            Min = c[i]
            idx = i
    c[idx] += inp[1][j]
    print(f'Customer {j+1} Booking Van {idx+1} | {inp[1][j]} day(s)')
