a = [11, 4, 0, 12, 41, 33, 8, 7, 9]
n = len(a)
for i in range(1, n):
    ei = a[i]
    j = i-1
    while j >= 0 and ei < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = ei
print(a)
