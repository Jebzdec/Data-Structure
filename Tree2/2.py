class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.level = 0

    def __str__(self) -> str:
        return str(self.val)


class AVL_Tree(object):

    def insert(self, root, key):

        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


def closestValue(root, value):
    a = root.val
    k = root.left if value < a else root.right
    if k == None:
        return root.val
    b = closestValue(k, value)
    return min((a, b), key=lambda x: abs(value-x))


myTree = AVL_Tree()
root = None
inp = input('Enter Input : ').split('/')
inp[0] = [int(e) for e in inp[0].split()]
inp[1] = int(inp[1])
for e in inp[0]:
    root = myTree.insert(root, e)
    printTree90(root)
    print('--------------------------------------------------')

print(f'Closest value of {inp[1]} : {closestValue(root,inp[1]) }')
