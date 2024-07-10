class Queue:
    def __init__(self) -> None:
        self.items = []

    def enQueue(self, items):
        self.items.append(items)

    def deQueue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


q = Queue()

x = []
for i in range(5):
    x.append([0]*5)
x[0][2] = 4
print(x)
