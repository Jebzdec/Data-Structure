inp = input('Ticket Details: ').split()
for i in range(3):
    inp[i] = int(inp[i])
inp[-1] = int(inp[-1])
print()
for i in range(1, inp[2]+1):
    print(i, end='  ')
print()
row = 65 + inp[1]-1  # A = 65
for i in range(row, 64, -1):
    for j in range(1, inp[2]+1):
        if chr(i) == inp[-2] and j == inp[-1]:
            print('x', end='  ')
        else:
            print('0', end='  ')
    print(chr(i), end='')
    print()


print(f'Theatre {inp[0]}')
if ord(inp[-2])-65 >= inp[1]-3:
    print(f'Price = 200')
else:
    print(f'Price = 180')
