def sort(i, j):
    if i-1 >= 0:
        if j-1 >= 0:
            if n[i] >= n[j-1]:
                temp = n[i]
                n[i] = n[j-1]
                n[j-1] = temp
            sort(i, j-1)
        else:
            sort(i-1, i-1)


def sort2(i, j):
    if i < l:
        if j+1 < l:
            if n[j+1] >= n[i]:
                temp = n[i+1]
                n[i+1] = n[i]
                n[i] = temp
            sort2(i, j+1)
        else:
            sort2(i+1, i+1)


n = list(map(int, input("Enter your list : ").split(',')))
l = len(n)
# sort(l-1, l-1)

sort2(0, 0)

# for i in range(len(n)):
#     for i in range(len(n)-i)
print(n)
