class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root:
            r = self.root
            while r:
                if val > r.data:
                    if r.right:
                        r = r.right
                    else:
                        r.right = Node(val)
                        return self.root
                else:
                    if r.left:
                        r = r.left
                    else:
                        r.left = Node(val)
                        return self.root
        else:
            self.root = Node(val)
            return self.root

    def delete(self, r, data):

        if r is None:
            print('Error! Not Found DATA')
            return r

        if data < r.data:
            r.left = self.delete(r.left, data)
        elif data > r.data:
            r.right = self.delete(r.right, data)
        else:
            if not r.left:
                return r.right
            elif not r.right:
                return r.left

            temp = Min(r.right)
            r.data = temp.data
            r.right = self.delete(r.right, temp.data)

        return r


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


def Min(node):
    if node.left == None:
        return node
    return Min(node.left)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for e in data:
    f = e.split()
    f[1] = int(f[1])
    if f[0] == 'd':
        print(f'delete {f[1]}')
        tree.root = tree.delete(tree.root, f[1])
    elif f[0] == 'i':
        print(f'insert {f[1]}')
        tree.insert(f[1])
    printTree90(tree.root)
