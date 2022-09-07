class Queue:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


data, question = input("Enter Input : ").split('/')
data = data.split(',')
question = question.split(',')
employee = {}
q = Queue()
for i in data:
    try:
        d, Id = map(int, i.split())
        employee[Id] = d
    except:
        pass

for i in question:
    try:
        f, Id = i.split()
        Id = int(Id)
    except:
        f = i[0]
        Id = None
    if f == 'D':
        if q.isEmpty():
            print('Empty')
        else:
            print(q.pop())
    elif f == 'E' and Id != None:
        copy = Queue()
        insert = False
        while not q.isEmpty():
            p = q.pop()
            if employee[p] == employee[Id]:
                insert = True
            else:
                if insert == True:
                    copy.push(Id)

            copy.push(p)

            if employee[p] == employee[Id] and q.isEmpty() and insert == True:
                copy.push(Id)

        if insert == False:
            copy.push(Id)
        q = copy
        # print([i for i in q.items], end=' ')
        # print(insert)
