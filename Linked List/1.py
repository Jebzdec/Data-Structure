class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def __str__(self):
        string = ""
        node = self.head
        while node != None:
            string += str(node.data)
            node = node.next
            if node != None:
                string += "->"
        return "link list : "+string

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        cur_node = self.head
        if cur_node:
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = Node(data)
        else:
            self.head = Node(data)

    def insert(self, index, data):
        count = -1
        cur_node = self.head
        new_node = Node(data)
        while cur_node.next != None:
            if count+1 == index:
                new_node.next = cur_node.next
                cur_node.next = new_node
        
                return f"index = {index} and data = {data}"
            cur_node = cur_node.next
            count += 1
        return 'Data cannot be added'


ll = LinkedList()

Input = input("Enter Input : ").split(',')
lst = list(map(int, Input[0].split()))
Input.pop(0)
for item in lst:
    ll.append(item)

print(str(ll))
for i in Input:
    i = i.strip(' ')
    idx, v = map(int, i.split(':'))
    print(ll.insert(idx, v))
    print(str(ll))
