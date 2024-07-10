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
        self.count = 0

    def printLL(self, i):
        s = ""
        node = self.head.next
        cnt = 0
        ap = False
        while node.next != None:
            if cnt == i:
                s += '| '
                ap = True
            s += str(node.data)+" "
            node = node.next
            cnt += 1
        if ap is False:
            s += '| '
        return s

    def insert(self, data, i):
        node = self.head.next
        for _ in range(i):
            node = node.next
        new = Node(data)
        new.next = node
        new.prev = node.prev
        node.prev.next = new
        node.prev = new

        self.count += 1

    def delete(self, i):
        if i >= 0 and i < self.count:
            cur = self.head
            cur = cur.next
            cnt = 0
            while cnt < i:
                cur = cur.next
                cnt += 1
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            self.count -= 1
            return True
        else:
            return False

    def size(self):
        return self.count


ll = LinkedList()
inp = input("Enter Input : ").split(',')
cursor = 0
for e in inp:
    if e[0] == "I":
        ll.insert(e[2:], cursor)
        cursor += 1
    elif e[0] == "L":
        if cursor-1 >= 0:
            cursor -= 1
    elif e[0] == "R":
        if cursor+1 <= ll.size():
            cursor += 1
    elif e[0] == "B":
        if ll.delete(cursor-1):
            cursor -= 1
    elif e[0] == "D":
        if ll.delete(cursor):
            pass
print(ll.printLL(cursor))
