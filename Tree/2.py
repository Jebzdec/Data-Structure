class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return self.root
        else:
            r = self.root
            while r is not None:
                if data < r.data:
                    if r.left == None:
                        r.left = Node(data)
                        return self.root
                    else:
                        r = r.left
                else:
                    if r.right == None:
                        r.right = Node(data)
                        return self.root
                    else:
                        r = r.right

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


def Min(node):
    if node.left == None:
        return node.data
    return Min(node.left)


def Max(node):
    if node.right == None:
        return node.data
    return Max(node.right)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('--------------------------------------------------')

print(f'Min : {Min(root)}')
print(f'Max : {Max(root)}')
