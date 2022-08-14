class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

b = Node(4)
print(b.data)