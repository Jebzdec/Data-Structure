class Queue:
    def __init__(self, value):
        self.items = list(value)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


def encodemsg(q1, q2):
    copy = Queue(q2.items[:])
    size = q1.size()
    for i in range(size):
        c = q1.dequeue()
        k = copy.dequeue()
        copy.enqueue(k)
        enc = chr(ord(c)+k)

        if c.islower() and not enc.islower():
            enc = chr(ord(c)+k-26)
        elif c.isupper() and not enc.isupper():
            enc = chr(ord(c)+k-26)

        q1.enqueue(enc)

    return f'Encode message is :  {q1.items}'


def decodemsg(q1, q2):
    copy = Queue(q2.items[:])
    size = q1.size()
    for i in range(size):
        c = q1.dequeue()
        k = copy.dequeue()
        copy.enqueue(k)
        dc = chr(ord(c)-k)

        if c.islower() and not dc.islower():
            dc = chr(ord(c)-k+26)
        elif c.isupper() and not dc.isupper():
            dc = chr(ord(c)-k+26)

        q1.enqueue(dc)

    return f'Decode message is :  {q1.items}'


string, num = input("Enter String and Code : ").replace(" ", "").split(',')
q1 = Queue(string)
q2 = Queue(map(int, num))
print(encodemsg(q1, q2))
print(decodemsg(q1, q2))
