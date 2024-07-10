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


def preorder(root, k):
    if root:
        if root.data > k:
            root.data *= 3
        preorder(root.left, k)
        preorder(root.right, k)


T = BST()
inp = input('Enter Input : ').split('/')
inp[0] = [int(i) for i in inp[0].split()]
inp[1] = int(inp[1])
# inp[0] = list(map(int, inp[0].split()))
for i in inp[0]:
    root = T.insert(i)
T.printTree(root)
preorder(root, inp[1])
print('--------------------------------------------------')
T.printTree(root)
