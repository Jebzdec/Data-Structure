print("*** Minesweeper ***")
lst_input = []

input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:

    lst_input.append([i for i in e.split()])

print("\n", *lst_input, sep="\n")

cnt = [[0]*5 for i in range(5)]

def check(x, y):
    if x >= 0 and y >= 0 and x < 5 and y < 5 and lst_input[x][y] != '#':
        cnt[x][y] = cnt[x][y] + 1

for i in range(5):
    for j in range(5):
        if (lst_input[i][j] == '#'):
            cnt[i][j] = '#'
            check(i-1, j-1)
            check(i-1, j)
            check(i-1, j+1)
            check(i, j-1)
            check(i, j+1)
            check(i+1, j-1)
            check(i+1, j)
            check(i+1, j+1)

cnt = [[str(cnt[i][j]) for j in range(5)] for i in range(5)]
print("\n", *cnt, sep='\n')
