def permu(x):
    if x == 0:
        print(ans)
        return
    for i in range(1, num+1):
        if i not in ans:
            ans.append(i)
            permu(x-1)
            ans.pop()


ans = []
num = int(input())
permu(num)
