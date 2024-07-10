n = int(input())
for i in range(-n+1, n):
    for j in range(-n+1, n):
        r = abs(i)+1
        c = abs(j)+1
        print(r if c < r else c, end='')
    print()
