inp = list(map(int, input("Enter Input : ").split()))
for i in range(len(inp)):
    for j in range(i):
        if inp[i] < 0 or inp[j] < 0:
            continue
        if inp[j] > inp[i]:
            temp = inp[i]
            inp[i] = inp[j]
            inp[j] = temp
print(*inp)
