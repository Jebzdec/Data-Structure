l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "merge sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l = list(map(int, l))
    lst = []
    for i in range(len(l)):
        j = 0
        front = False
        for j in range(len(lst)):
            print(l[i], lst[j])
            if l[i] < lst[j]:
                front = True
                lst.insert(j, l[i])
                break
        if front == False:
            lst.insert(j+1, l[i])
        n = len(lst)-1
        x = int(n/2)
        if n % 2 == 0:
            med = lst[x]
        else:
            # print(lst)
            med = lst[x]+lst[x+1]
            med /= 2
        print(f'list = {l[0:i+1]} : median = '+"%.1f" % med)
