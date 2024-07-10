    def append(self, data):
        new = Node(data)
        tail = self.tail
        tail.prev.next = new
        tail.prev = new
        new.prev = tail.prev
        new.next = tail