def check(l):
    for i in range(1, len(l)-1):
        if l[i] < l[i-1]:
            return 'No'
    return 'Yes'


inp = list(map(int, input("Enter Input : ").split()))
print(check(inp))
