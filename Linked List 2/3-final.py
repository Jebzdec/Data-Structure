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
            s += str(node.data)+' '
            node = node.next
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

    def merge(self, l):
        tail = l.tail
        while tail is not l.head:
            self.append(tail.data)
            tail = tail.prev

    def merge(self, l):
        tail = self.tail
        new = l.tail
        while new is not l.head:
            # new.next = tail
            # new.prev = tail.prev
            # tail.prev.next = new
            # tail.prev = new
            print(tail.data.prev)
            new = new.prev


inp = input('Enter Input (L1,L2) : ').split()
l1 = inp[0].split('->')

l2 = inp[1].split('->')

ll1 = LinkedList()
ll2 = LinkedList()
for e in l1:
    ll1.append(e)

for e in l2:
    ll2.append(e)

print(f'L1    : {ll1}')
print(f'L2    : {ll2}')
ll1.merge(ll2)
print(f'Merge : {ll1}')
