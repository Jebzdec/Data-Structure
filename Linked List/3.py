class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.head.next = Node()

    def __str__(self) -> str:
        node = self.head.next
        s = ''
        while node.next is not None:
            s += str(node.data)
            node = node.next

        return s

    def append(self, data):
        cur_node = self.head
        new = Node(data)
        while cur_node.next.data is not None:
            cur_node = cur_node.next
        new.prev = cur_node
        new.next = cur_node.next
        cur_node.next.prev = new
        cur_node.next = new

    def reversed(self, data):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next

        while cur_node.prev is not None:
            pass

        return f'Merge : {str(self)}'


Input = input('Enter Input (L1,L2) : ').split()

list1 = Input[0].split('->')
list2 = Input[1].split('->')

LL1 = LinkedList()
for i in list1:
    for j in i:
        LL1.append(j)
    LL1.append(' ')
print(f'L1    : {LL1}')

LL2 = LinkedList()
for i in list2:
    for j in i:
        LL2.append(j)
    LL2.append(' ')
print(f'L2    : {LL2}')

for i in range(len(list2)-1, -1, -1):
    for j in list2[i]:
        LL1.append(j)
    LL1.append(' ')
print(f'Merge : {str(LL1)}')
