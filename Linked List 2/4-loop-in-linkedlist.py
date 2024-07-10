class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.tail.prev = self.head
        self.head.next = self.tail
        self.loop = False

    def __str__(self) -> str:
        s = ""
        node = self.head.next
        while node is not self.tail:
            s += str(node.data)
            node = node.next
            if node is not self.tail:
                s += '->'
        return s

    def append(self, data):
        new = Node(data)
        tail = self.tail
        new.next = tail
        new.prev = tail.prev
        tail.prev.next = new
        tail.prev = new
        return str(self)

    def isEmpty(self):
        return True if self.head.next is self.tail else False

    def set_next(self, first, second):
        try:
            node1 = self.getNode(first)
        except:
            if self.isEmpty():
                return f'Error! {{list is empty}}'
            else:
                return f'Error! {{index not in length}}: {first}'
        try:
            node2 = self.getNode(second)
        except:
            self.append(second)
            return f'index not in length, append : {second}'

        if first >= second:
            self.loop = True
        s = f'Set node.next complete!, index:value = {first}:{self[first]} -> {second}:{self[second]}'
        node1.next = node2
        return s

    def getNode(self, index):
        node = self.head
        for _ in range(index+1):
            node = node.next
            if node.data == None:
                raise Exception()
        return node

    def __getitem__(self, index):
        node = self.head
        for _ in range(index+1):
            node = node.next
            if node.data == None:
                raise Exception()
        return node.data


ll = LinkedList()

inp = input("Enter input : ").split(',')

for i in inp:
    f, v = i.split()
    v = list(map(int, v.split(':')))
    if f == 'A':
        print(ll.append(v[0]))
    elif f == 'S':
        print(ll.set_next(v[0], v[1]))

if ll.loop == False:
    print('No Loop')
    print(ll)
else:
    print('Found Loop')
