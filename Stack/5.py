class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def forest(key, value):
    global tree
    global cnt
    global Max
    copy = Stack()
    if key == 'A':
        tree.push(value)
    elif key == 'B':
        while not tree.isEmpty():
            if tree.peek() > Max:
                cnt += 1
                Max = tree.peek()
            copy.push(tree.peek())
            tree.pop()

        while not copy.isEmpty():
            tree.push(copy.peek())
            copy.pop()

        print(cnt)
        cnt = 0
        Max = -1
    elif key == 'S':
        for i in range(tree.size()):
            if tree.items[i] % 2 == 0:
                tree.items[i] -= 1
            else:
                tree.items[i] += 2


tree = Stack()
cnt = 0
Max = -1
Input = input("Enter Input : ").split(',')
for i in Input:
    try:
        k, h = i.split()
    except:
        k = i[0]
        h = -1
    forest(k, int(h))
