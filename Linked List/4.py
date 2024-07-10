# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#         self.prev = None


# class LinkedList:
#     def __init__(self):
#         self.head = Node()
#         self.head.next = Node()
#         self.count = 0

#     def printLL(self, i):
#         s = ""
#         cur_node = self.head.next
#         cnt = 0
#         ap = False
#         while cur_node.next != None:
#             if cnt == i:
#                 s += '| '
#                 ap = True
#             s += str(cur_node.data)+" "
#             cur_node = cur_node.next
#             cnt += 1
#         if ap is False:
#             s += '| '
#         return s

#     def append(self, data, i):
#         cur_node = self.head
#         new_node = Node(data)
#         cnt = 0
#         while cnt < i:
#             cur_node = cur_node.next
#             cnt += 1
#         cur_node.next.prev = new_node
#         new_node.prev = cur_node
#         new_node.next = cur_node.next
#         cur_node.next = new_node
#         self.count += 1

#     def delete(self, i):
#         if i >= 0 and i < self.count:
#             cur_node = self.head
#             cur_node = cur_node.next
#             cnt = 0
#             while cnt < i:
#                 cur_node = cur_node.next
#                 cnt += 1
#             cur_node.prev.next = cur_node.next
#             cur_node.next.prev = cur_node.prev
#             self.count -= 1
#             return True
#         else:
#             return False

#     def size(self):
#         return self.count


# ll = LinkedList()
# inp = input("Enter Input : ").split(',')
# cursor = 0
# for e in inp:
#     if e[0] == "I":
#         ll.append(e[2:], cursor)
#         cursor += 1
#     elif e[0] == "L":
#         if cursor-1 >= 0:
#             cursor -= 1
#     elif e[0] == "R":
#         if cursor+1 <= ll.size():
#             cursor += 1
#     elif e[0] == "B":
#         if ll.delete(cursor-1):
#             cursor -= 1
#     elif e[0] == "D":
#         if ll.delete(cursor):
#             pass
# print(ll.printLL(cursor))
