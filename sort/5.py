def subset_sum(numbers, target, partial=[], lst=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        lst.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n], lst)

    return lst


def swap(a, b):
    return b, a


su, lst = input("Enter Input : ").split('/')
lst = list(map(int, lst.split()))
for i in range(len(lst)):
    for j in range(i):
        if lst[j] > lst[i]:
            # print(lst[i], e)
            lst[i], lst[j] = swap(lst[i], lst[j])
lst = subset_sum(lst, int(su))
for i in range(len(lst)):
    for j in range(i):
        comp = len(lst[j]) - len(lst[i])
        if comp > 0:
            lst[i], lst[j] = swap(lst[i], lst[j])
        elif comp == 0:
            for k in range(0, len(lst[j])):
                if lst[i][k] < lst[j][k]:
                    # print(lst[i], lst[i][k], lst[j], lst[j][k])
                    lst[i], lst[j] = swap(lst[i], lst[j])
                    break
                elif lst[i][k] > lst[j][k]:
                    break
if len(lst) > 0:
    print(*lst, sep='\n')
else:
    print('No Subset')
