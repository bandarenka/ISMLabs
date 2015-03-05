class Generator:
    def __init__(self, a, c, M, x1):
        self.a = a
        self.c = c
        self.M =  M
        self.cur = x1
       
    def generate(self):
        self.cur = (self.a * self.cur + self.c) % self.M
        return self.cur

    def generateList(self, n):
        res = [self.cur]
        for i in range(1,n + 1):
            res.append(self.generate())
        return res


class McLarenGen:
    V = []
    def __init__(self, X, Y, k):
        self.X = X
        self.Y = Y
        self.k = k
        self.M = Y.M
        for i in range(0,k-1):
            self.V.append(self.X.generate())
    
    def generate(self):
        j = (self.k - 1) * self.Y.generate() // self.Y.M
        cur = self.V[j]
        self.V[j] = self.X.generate()
        return cur

    def generateList(self, n):
        res = []
        for i in range(1,n):
            res.append(self.generate())
        return res

def continuous(x, n):
    res = []
    list = x.generateList(n)
    m = max(list)
    for i in list:
        res.append(i / (m + 1))
    return res
    
def discrete(x, n, N):
    res = []
    contin = continuous(x, n)
    for i in contin:
        k = int(i * N)
        if i * N - k > 0.5:
            k = k + 1
        res.append(k)
    return res