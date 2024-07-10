class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.head.next = Node()

    def __str__(self):
        string = ""
        node = self.head.next
        while node.next != None:
            string += str(node.data)
            node = node.next
            if node.data != None:
                string += "->"
        return "linked list : "+string

    def str__reverse(self):
        node = self.head
        while node.next.data != None:
            node = node.next
        string = ""
        while node.previous != None:
            string += str(node.data)
            node = node.previous
            if node.data != None:
                string += "->"
        return "reverse : " + string

    def isEmpty(self):
        return self.head.next == None

    def add_before(self, data):
        cur_node = self.head
        new_node = Node(data)

        cur_node.next.previous = new_node
        new_node.next = cur_node.next
        new_node.previous = cur_node
        cur_node.next = new_node

    def append(self, data):
        cur_node = self.head
        new_node = Node(data)

        while cur_node.next.data != None:
            cur_node = cur_node.next

        cur_node.next.previous = new_node
        new_node.next = cur_node.next
        new_node.previous = cur_node
        cur_node.next = new_node

    def insert(self, index, data):
        count = -1
        cur_node = self.head
        new_node = Node(data)
        while cur_node.next != None:
            if count+1 == index:
                cur_node.next.previous = new_node
                new_node.next = cur_node.next
                new_node.previous = cur_node
                cur_node.next = new_node
                return f"index = {index} and data = {data}"
            cur_node = cur_node.next
            count += 1
        return 'Data cannot be added'

    def remove(self, data):
        node = self.head
        count = -1
        while node.next != None:
            if node.data == data:
                node.previous.next = node.next
                node.next.previous = node.previous
                return f"removed : {data} from index : {count}"
            node = node.next
            count += 1
        return "Not Found!"


ll = LinkedList()

Input = input("Enter Input : ").split(',')

for i in Input:
    f, n = i.split()
    n = list(map(int, n.split(':')))
    if f == 'R':
        print(ll.remove(n[0]))
    elif f == 'I':
        print(ll.insert(n[0], n[1]))
    elif f == 'Ab':
        ll.add_before(n[0])
    elif f == 'A':
        ll.append(n[0])

    print(str(ll))
    print(ll.str__reverse())
