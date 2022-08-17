s = []


def ManageStack(key, value):
    global s
    copy = []
    rev = list(reversed(s))
    if key == 'A':
        s.append(value)
        print(f'Add = {value}')
    elif key == 'P':
        if s == []:
            print('-1')
        else:
            print(f'Pop = {s[-1]}')
            s.pop()
    elif key == 'D':
        if s == []:
            print('-1')
        else:
            for i in rev:
                if i == value:
                    print(f'Delete = {i}')
                else:
                    copy.append(i)
            s = list(reversed(copy))
    elif key == 'LD':
        if s == []:
            print('-1')
        else:
            for i in rev:
                if i < value:
                    print(f'Delete = {i} Because {i} is less than {value}')
                else:
                    copy.append(i)
            s = list(reversed(copy))
    elif key == 'MD':
        if s == []:
            print('-1')
        else:
            for i in rev:
                if i > value:
                    print(f'Delete = {i} Because {i} is more than {value}')
                else:
                    copy.append(i)
            s = list(reversed(copy))


Input = input("Enter Input : ").split(',')
for item in Input:
    try:
        k, v = item.split()
        ManageStack(k, int(v))
    except:
        k = item
        if k == 'P':
            ManageStack(k, None)

    # print(k,v)

print(f'Value in Stack = {s}')
