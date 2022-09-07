class queue:
    def __init__(self):
        self.items = []

    def enQueue(self, value):
        self.items.append(value)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def front(self):
        return self.items[0]


q = queue()
q1 = queue()
q2 = queue()
sec = 1
sec1 = -1
sec2 = -1
s = input('Enter people : ')
for i in s:
    q.enQueue(i)

while not q.isEmpty():

    if not q1.isEmpty() and sec - sec1 == 3:
        q1.deQueue()
        sec1 = sec
    if not q2.isEmpty() and sec - sec2 == 2:
        q2.deQueue()
        sec2 = sec

    if q1.size() < 5:
        q1.enQueue(q.front())
        q.deQueue()
        if sec1 == -1:
            sec1 = sec
    else:
        if q2.size() < 5:
            q2.enQueue(q.front())
            q.deQueue()
            if sec2 == -1:
                sec2 = sec

    print(f'{sec} {q.items} {q1.items} {q2.items}')
    sec += 1
