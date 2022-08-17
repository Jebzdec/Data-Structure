class Stack:

    def __init__(self):
        self.item = []
    def push(self, value):
        self.item.append(value)
    def pop(self):
        self.item.pop
    def size(self):
        return self.item[-1]
    def isEmpty(self):
        return self.item == []
inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')

### Enter Your Code Here ###

while not S.isEmpty():

    print(S.pop(), end='')

print()