class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.right = None
        self.down = None
        self.top = None
        self.count_child = None


def digit(num, i):
    if num >= 0:
        return (num//i) % 10
    else:
        return (num*-1//i) % 10


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.head.right = Node()

    def print_right(self):
        s = ""
        node = self.head
        while node.right is not None:
            s += str(node.data) + " "
            node = node.right
        return s

    def print_down(self, node, spc=""):
        s = ""
        node = node.down
        while node.down is not None:
            s += str(node.data) + " "
            node = node.down
            if node.down is not None:
                s += spc
        return s

    def print_up(self, node, spc="", Pos=0):
        s = ""
        while node.down.down is not None:
            node = node.down
        while node.top is not None:
            s += str(node.data) + " "
            node = node.top
            if node.data is not None or Pos > 0:
                s += spc
        return s

    def add_right(self, data):
        node = self.head
        new_node = Node(data)
        while node.right.right is not None:
            node = node.right
        new_node.right = node.right
        node.right = new_node
        tail = Node()
        tail.top = node
        node.down = tail

    def add_down(self, node, data):
        new_node = Node(data)
        cnt = 0
        while node.down.down is not None:
            cnt += 1
            node = node.down
        new_node.top = node
        new_node.down = node.down
        node.down.top = new_node
        node.down = new_node

    def find(self, i):
        node = self.head
        cnt = -1
        while node.right is not None and cnt < i:
            node = node.right
            cnt += 1
        return node

    def count_child(self, node):
        l = 0
        node = node.down
        while node.down is not None:
            l += 1
            node = node.down
        return l

    def remove(self, node):
        node.top.down = node.down
        node.down.top = node.top

    def radix_sort(self, k):
        node = self.head.right
        while node.right.right is not None:
            node.count_child = self.count_child(node)
            node = node.right
        node = self.head.right
        while node.right.right is not None:
            i = 0
            child = node.down
            while i < node.count_child:
                # print(self.print_all())
                #     print(f'child {child.data} -> {child.down.data}')
                d = digit(child.data, k)
                digit_node = self.find(d)
                if child.data >= 0:
                    self.add_down(digit_node, child.data)
                else:
                    self.add_down(digit_node, child.data)
                self.remove(child)
                child = child.down
                i += 1
            node = node.right

    def print_all(self):
        node = pos.head
        i = -1
        while node.right.right is not None:
            child = node.down
            print(i, end=' | ')
            while child.down is not None:
                print(child.data, end=' -> ')
                child = child.down
            print()
            node = node.right
            i += 1


inp = list(map(int, input("Enter Input : ").split()))
pos = LinkedList()
neg = LinkedList()
Max = float('-inf')
k = 1
for i in range(0, 11):
    pos.add_right(None)
    neg.add_right(None)

for e in inp:
    l = len(str(e))
    if e == 0:
        l = 0
    if e >= 0:
        pos.add_down(pos.find(digit(e, k)), e)
    else:
        l -= 1
        neg.add_down(neg.find(digit(e, k)), e)

    if l > Max:
        Max = l

print('------------------------------------------------------------')
if Max > 0:
    for i in range(0, Max):
        print(f'Round : {i+1}')
        pos.radix_sort(k)
        neg.radix_sort(k)
        for j in range(0, 10):
            print(f'{j} : {neg.print_up(neg.find(j))}', end='')
            print(f'{pos.print_down(pos.find(j))}')
        print('------------------------------------------------------------')
        k *= 10
    pos.radix_sort(k)
    neg.radix_sort(k)
print(f'{Max} Time(s)')
print(f'Before Radix Sort : ', end='')
print(*inp, sep=' -> ')
print(f'After  Radix Sort : ', end='')
p = pos.print_down(pos.find(0), "-> ")
s = neg.print_up(neg.find(0), "-> ", len(p))
print(s, end='')
print(p, )
