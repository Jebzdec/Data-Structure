from ast import Global


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def ManageStack(key, value):
    global s
    copy = []
    if key == 'A':
        s.push(value)
        print(f'Add = {value}')
    elif key == 'P':
        if s.isEmpty():
            print('-1')
        else:
            print(f'Pop = {s.peek()}')
            s.pop()
    elif key == 'D':
        if s.isEmpty():
            print('-1')
        else:
            for i in s:
                if i == value:
                    print(f'Delete = {i}')
                else:
                    copy.append(i)
            s = copy
    elif key == 'LD':
        if s.isEmpty():
            print('-1')
        else:
            for i in s:
                if i < value:
                    print(f'Delete = {i} Because {i} is less than {value}')
                else:
                    copy.append(i)
            s = copy
    elif key == 'MD':
        if s == []:
            print('-1')
        else:
            for i in s:
                if i > value:
                    print(f'Delete = {i} Because {i} is more than {value}')
                else:
                    copy.append(i)
            s = copy


Input = input("Enter Input : ").split(',')
s = Stack()
for item in Input:
    try:
        k, v = item.split()
    except:
        k = item
        v = 0
    ManageStack(k, int(v))

print(f'Value in Stack = {s}')
