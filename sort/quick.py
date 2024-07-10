def quick(l, left, right):
    """last element pivot"""
    if left == right+1:  # only 2 elements
        if l[left] > l[right]:
            l[left], l[right] = l[right], l[left]  # swap
        return
    if left < right:
        # partition
        pivot = l[right]  # last element pivot
        print('-------------------------------------')
        print(' 0 1 2 3 4 5 6 7 8 9 ',
              ' (left=', left, ' right=', right, ' pivot=', pivot, ')', sep='')
        print(l)
        i, j = left, right-1
        while i < j:
            while i < right and l[i] <= pivot:
                i += 1
            while j > left and l[j] >= pivot:
                j -= 1
            if i < j:
                l[i], l[j] = l[j], l[i]  # swap
                print(l, '(swap', l[i], '-', l[j], ')')
        if right is not i:
            l[right], l[i] = l[i], pivot  # swap pivot to index i
            print(l, '(swap pivot', l[i], '-', l[right], ')')
        quick(l, left, i-1)
        quick(l, i+1, right)


l = [5, 1, 4, 9, 0, 3, 8, 2, 7, 6]
print('Quick Sort : pivot=last element')
print(' 0 1 2 3 4 5 6 7 8 9')
print(l)
quick(l, 0, len(l)-1)
print('output list :')
print(l)
