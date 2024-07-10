from select import select


class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def push(self,items):
        self.items.append(items)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

s = Stack()
lst = [1,2,3,4,5]
for i in lst:
    s.push(i)

while not s.isEmpty():
    print(s.pop() )