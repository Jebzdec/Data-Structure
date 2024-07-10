def TowerOfHanoi(n, from_rod, aux_rod, to_rod):
    if n == 0:
        return

    TowerOfHanoi(n-1, from_rod, to_rod, aux_rod)
    printTower(0, num)
    if l[from_rod] != []:
        l[from_rod].pop()
        l[to_rod].append(n)
    print(f'\nmove {n} from  {tower[from_rod]} to {tower[to_rod]}')

    TowerOfHanoi(n-1, aux_rod, from_rod, to_rod)


def printTower(i, j):
    try:
        print(f'{l[i][j]} ', end=' ')
    except:
        print('| ', end=' ')
    if i+1 < 3:
        printTower(i+1, j)
    else:
        if j - 1 >= 0:
            print()
            printTower(0, j-1)


tower = ['A', 'B', 'C']
num = int(input('Enter Input : '))
l = [[]*3 for _ in range(3)]
for i in range(num, 0, -1):
    l[0].append(i)
TowerOfHanoi(num, 0, 1, 2)
printTower(0, num)
