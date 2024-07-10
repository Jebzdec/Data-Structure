class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, data):
        new = Node(data)
        tail = self.tail
        new.prev = tail.prev
        new.next = tail
        tail.prev.next = new
        tail.prev = new

    def __getitem__(self, index):
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur.data

    def __getattribute__(self, index):
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
        return cur

ll = LinkedList()
for i in range(0, 10):
    ll.append(i)

for i in range(10):
    print(ll[i])


