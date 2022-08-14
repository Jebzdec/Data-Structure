print("*** Fun with countdown ***")
lst = list(map(int, input("Enter List : ").split()))
sub = []
ans_lst = []
for i in lst:
    if len(sub) == 0:
        sub.append(i)
    else:
        if i != sub[-1]-1:
            sub.clear()
        sub.append(i)
    if len(sub) > 0 and sub[-1] == 1:
        ans_lst.append(str(sub))
        sub.clear()
print(f'[{len(ans_lst)}, [',end='')
print(*ans_lst, sep=', ',end='')
print(']]')
