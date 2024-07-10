class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        s = ""
        node = self.head.next
        while node is not self.tail:
            s += str(node.data)
            node = node.next
            if node is not self.tail:
                s += '->'
        return s

    def str_reverse(self):
        s = ""
        node = self.tail.prev
        while node is not self.head:
            s += str(node.data)
            node = node.prev
            if node is not self.head:
                s += '->'
        return s

    def append(self, data):
        new = Node(data)
        tail = self.tail
        new.next = tail
        new.prev = tail.prev
        tail.prev.next = new
        tail.prev = new

    def isEmpty(self):
        return True if self.head.next == self.tail else False

# cur
    def insert(self, index, data):
        i = 0
        node = self.head.next
        new = Node(data)
        while node is not None:
            if i == index:
                new.next = node
                new.prev = node.prev
                node.prev.next = new
                node.prev = new
                return f'index = {i} and data = {data}'
            node = node.next
            i += 1
        return 'Data cannot be added'

    def remove(self, data):
        node = self.head.next
        i = 0
        while node is not self.tail:
            if node.data == data:
                node.prev.next = node.next
                node.next.prev = node.prev
                return f'removed : {data} from index : {i}'
            node = node.next
            i += 1
        return 'Not Found!'


ll = LinkedList()
inp = input("Enter Input : ").split(',')
for i in inp:
    f, v = i.split()
    v = list(map(int, v.split(':')))
    if f == 'A':
        ll.append(v[0])
    elif f == 'Ab':
        ll.insert(0, v[0])
    elif f == 'R':
        print(ll.remove(v[0]))
    elif f == 'I':
        print(ll.insert(v[0], v[1]))
    print('linked list :', ll)
    print('reverse : '+ll.str_reverse())
