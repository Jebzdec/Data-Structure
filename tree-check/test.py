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
        r = self.root
        if r == None:
            self.root = Node(data)
        else:
            while r != None:
                if data > r.data:
                    if r.right == None:
                        r.right = Node(data)
                        break
                    r = r.right
                else:
                    if r.left == None:
                        r.left = Node(data)
                        break
                    r = r.left

        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
