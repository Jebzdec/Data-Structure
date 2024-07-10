class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        s = ""
        for i in self.items:
            s += str(self.items)
        return s

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def top(self):
        return self.items[-1]


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level+1)
        print('     ' * level, node)
        printTree(node.left, level+1)


def inorder(root):
    if root != None:
        if root.left and root.right:
            print('(', end='')
        inorder(root.left)
        print(root.data, end='')
        inorder(root.right)
        if root.left and root.right:
            print(')', end='')


def preorder(root):
    if root != None:
        print(root.data, end='')
        preorder(root.left)
        preorder(root.right)


stack = Stack()
inp = input('Enter Postfix : ')
for e in inp:
    if e == '+' or e == '-' or e == '*' or e == '/':
        op = Node(e)
        a = stack.pop()
        b = stack.pop()
        op.left = b
        op.right = a
        stack.push(op)
    else:
        stack.push(Node(e))

print('Tree :')
printTree(stack.top())
print('--------------------------------------------------')
print('Infix : ', end='')
inorder(stack.top())
print()
print('Prefix : ', end='')
preorder(stack.top())
