class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None


def digit(num, i):
    if num>=0:
        return (num//i) %10
    else:
        return (num*-1//i) %10

class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.head.next = Node()

    def __str__(self) -> str:
        node = self.head.next
        s = ""
        while node.next is not None:
            s += str(node.data)+" "
            node = node.next
        return s

    def append(self, data):
        cur_node = self.head
        new_node = Node(data)
        while cur_node.next.next is not None:
            cur_node = cur_node.next
        cur_node.next.prev = new_node
        new_node.prev = cur_node
        new_node.next = cur_node.next
        cur_node.next = new_node

    def insert(self, data, k, pos):
        cur_node = self.head
        new_node = Node(data)
        while cur_node.next.next is not None:
            if pos is True and digit(data, k) > digit(cur_node.next.data, k):
                break
            else:
                if digit(data, k) < digit(cur_node.next.data, k):
                    break
            cur_node = cur_node.next

        new_node.next = cur_node.next
        new_node.prev = cur_node
        cur_node.next.prev = new_node
        cur_node.next = new_node

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def sort(self, k):
        cur_node = self.head.next
        while cur_node.next.next is not None:
            self.delete(cur_node)
            self.insert(cur_node.data, k,
                        True if cur_node.data >= 0 else False)
            cur_node = cur_node.next

    def findByDigit(self,k,num):
        node = self.head.next
        s = ""
        while node.next is not None:
            if digit(node.data,k) == num:
                s += str(node.data)+" "
                #print(digit(node.data,k))
            node = node.next
        return s



inp = list(map(int, input("Enter Input : ").split()))
pos = LinkedList()
neg = LinkedList()
Max = float('-inf')
k = 1
for i in range(0, len(inp)):
    if inp[i] >= 0:
        l = len(str(inp[i]))
        if l > Max:
            Max = l
        if i == 0:
            pos.append(inp[i])
        else:
            pos.insert(inp[i], k, True)
    else:
        l = len(str(inp[i]))-1
        if l > Max:
            Max = l
        if i == 0:
            neg.append(inp[i])
        else:
            neg.insert(inp[i], k, False)

for i in range(0, Max):
    print(
        f'------------------------------------------------------------\nRound : {i+1}')
    pos.sort(k)
    neg.sort(k)
    for j in range(0,10):
        print(f'{j} : {neg.findByDigit(k,j)}',end='')
        print(f'{pos.findByDigit(k,j)}')
    k *= 10

