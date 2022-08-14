output = []
def Sum(a):
    for i in range(len(a)):
        for j in range(i):
            for k in range(j):
                if a[i]+a[j]+a[k] == 0:
                    output.append(f'[{a[k]}, {a[j]}, {a[i]}]')


list_input = list(map(int, input("Enter Your List : ").split()))
if len(list_input)<3 :
    print("Array Input Length Must More Than 2")
else : 
    Sum(list_input)
    output = [*set(output)]
    print('[',end='')
    print(*output,sep=', ',end='')
    print(']',end='')