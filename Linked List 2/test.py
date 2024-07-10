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

    def __str__(self) -> str:
        node = self.head.next
        s = ""
        while node is not self.tail:
            s += node.data+' '
            node = node.next
        return s

    def append(self, data):
        new = Node(data)
        tail = self.tail
        new.prev = tail.prev
        new.next = tail
        tail.prev.next = new
        tail.prev = new

    def 

ll = LinkedList()
inp = input().split()
for i in inp:
    ll.append(i)
print(ll)
