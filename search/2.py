def bi_search(l, r, arr, x):
    m = int((l+r)/2)

    if l <= r:
        if arr[m] == x:
            if m+1 < len(arr):
                return arr[m+1]
            return 'No First Greater Value'
        elif arr[m] < x:
            return bi_search(m+1, r, arr, x)
        else:
            if arr[m-1] < x:
                return arr[m]
            return bi_search(l, m-1, arr, x)
    else:
        if l < len(arr) and arr[l] > x:
            return arr[l]
        return 'No First Greater Value'


inp = input('Enter Input : ').split('/')
arr = list(map(int, inp[0].split()))
k = list(map(int, inp[1].split()))
for e in k:
    print(bi_search(0, len(arr) - 1, sorted(arr), e))
