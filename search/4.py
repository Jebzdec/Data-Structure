def isPrime(n):
    m = int(n/2)
    for i in range(2, m):
        if n % i == 0:
            return False
    return True


class Hash:
    def __init__(self, arr):
        self.size = arr[0]
        self.max_col = arr[1]
        self.threshold = arr[2]
        self.used = 0
        self.data = [None]*self.size
        self.list = []

    def push(self, v):
        self.check_threshold()
        i = v % self.size
        if self.data[i] == None:
            self.used += 1
            self.data[i] = v
            self.list.append(v)
        else:
            self.collision(v, i)

    def collision(self, v, i, cnt=1):
        self.check_threshold()
        if cnt > self.max_col:
            print('****** Max collision - Rehash !!! ******')
            self.rehashing()
            cnt = 1
        i = (v + (cnt-1)*(cnt-1)) % self.size
        if self.data[i] == None:
            self.data[i] = v
            self.used += 1
            self.list.append(v)
        else:
            print(f'collision number {cnt} at {i}')
            self.collision(v, i, cnt+1)

    def check_threshold(self):
        if (self.used+1)/self.size >= self.threshold/100:
            print('****** Data over threshold - Rehash !!! ******')
            self.rehashing()

    def rehashing(self):
        new_size = self.size*2+1
        while True:
            if isPrime(new_size):
                break
            new_size += 1
        lst = []
        for e in self.data:
            if e != None:
                lst.append(e)
        self.data = [None]*(new_size)
        self.size = new_size
        self.used = 0
        lst = self.list
        self.list = []
        for e in lst:
            self.push(e)

    def print(self):
        for i in range(len(self.data)):
            print(f'#{i+1}\t{self.data[i]}')
        print('----------------------------------------')


print(' ***** Rehashing *****')
inp = input('Enter Input : ').split('/')
inp[0] = [int(i) for i in inp[0].split()]
inp[1] = [int(i) for i in inp[1].split()]
h = Hash(inp[0])
print('Initial Table :')
h.print()
for e in inp[1]:
    print('Add :', e)
    h.push(e)
    h.print()
