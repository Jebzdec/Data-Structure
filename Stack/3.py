class Stack:

    def __init__(self):
        self.item = []

    def push(self, value):
        self.item.append(value)

    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []


class Postfix(Stack):

    def push(self, value):
        if value != '(':
            return super().push(value)


def operator(c):

    if c == '^':
        return 0
    elif c == '*' or c == '/':
        return 1
    elif c == '+' or c == '-':
        return 2
    else:
        return 3


input = input('Enter Infix : ')
input = [i for i in input]

stack = Stack()
postfix = Postfix()

for i in input:
    if i == '(':
        stack.push(i)
    elif i == ')':
        while stack.peek() != '(':
            postfix.push(stack.pop())
        stack.pop()
    else:
        if operator(i) == 3:
            postfix.push(i)
        else:
            while not stack.isEmpty() and operator(stack.peek()) <= operator(i):
                postfix.push(stack.pop())
            stack.push(i)

while not stack.isEmpty():
    postfix.push(stack.pop())
print('Postfix : ',end='')
print(*postfix.item, sep='')
