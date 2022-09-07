class Stack:

    def __init__(self, list=None):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.size())

    def peek(self):
        return self.items[-1]


def infix2postfix(exp):

    s = Stack()
    s.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
    postfix = Stack()

    exp = [i for i in exp]
    for i in exp:
        if i == '(':
            s.push(i)
        elif i == ')':
            while s.peek() != '(':
                postfix.push(s.pop())
            s.pop()
        else:
            if i >= 'A' and i <= 'z':
                postfix.push(i)
            else:
                while not s.isEmpty() and s.precedence[i] <= s.precedence[s.peek()]:
                    postfix.push(s.pop())
                s.push(i)

    while not s.isEmpty():
        postfix.push(s.pop())
    return postfix.items


print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(*infix2postfix(token), sep='')
