class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        r = self.root
        while r != None:
            if data > r.data:
                r = r.right
            else:
                r = r.left
        r = Node(data)

    def travel(self, r, sum=0):
        if r.left == None and r.right == None:
            return r

        r = Min(self.travel(r.left), self.travel(r.right))
        r.right -= r
        r.left -= r
        sum += r.right + r.left
        return r


def Min(a, b):
    return a if a > b else b


bst = BST()
inp = input('Enter Input : ').split('/')
inp[0] = int(inp[0])
inp[1] = [int(e) for e in inp[1].split()]

if len(inp[1]) != int(inp[0]/2+1):
    print('Incorrect Input')
else:
    for i in range(1,len(inp[1])+1)
    for e in inp[1]:

