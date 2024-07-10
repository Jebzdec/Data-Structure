class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class hash:
    def __init__(self, table_size, max_collinsion):
        self.table_size = table_size
        self.data = [None]*table_size
        self.max_collinsion = max_collinsion
        self.used = 0

    def push(self,  k, v):
        i = self.get_index(k)
        if self.data[i] == None:
            self.data[i] = Data(k, v)
            self.used += 1
        else:
            self.collinsion(k, v, 1, i)

    def collinsion(self,  k, v, cnt, i):
        print(f'collision number {cnt} at {i}')
        i = (self.get_index(k)+cnt*cnt) % self.table_size
        if self.data[i] == None:
            self.data[i] = Data(k, v)
            self.used += 1
        else:
            if cnt+1 <= self.max_collinsion:
                self.collinsion(k, v, cnt+1, i)
            else:
                print('Max of collisionChain')

    def isFull(self):
        return self.used == self.table_size

    def get_index(self, k):
        sum = 0
        for e in k:
            sum += ord(e)
        return sum % self.table_size

    def print(self):
        for i in range(0, table_size):
            print(f'#{i+1}      {self.data[i]}')
        print('---------------------------')


print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
table_size, maxCollision = map(int, inp[0].split())
inp[1] = inp[1].split(',')
h = hash(table_size, maxCollision)
for e in inp[1]:
    k, v = e.split()
    h.push(k, v)
    h.print()
    if h.isFull():
        print('This table is full !!!!!!')
        break
