import math

class MauerTest:
   
    def __init__(self, gen, n, L, Q, seq = None):
        self.info = {6 : (5.2177052, 2.954),
                     7 : (6.1962507, 3.125),
                     8 : (7.1836656, 3.238),
                     9 : (8.1764248, 3.311),
                     10 : (9.1723243, 3.356),
                     11 : (10.170032, 3.384),
                     12 : (11.168765, 3.401),
                     13 : (12.168070, 3.410),
                     14 : (13.167693, 3.416),
                     15 : (14.167488, 3.419),
                     16 : (15.167379, 3.421) }
        self.gen = gen
        self.n = n
        self.L = L
        self.Q = Q
        self.K = (n - L * Q) // L
        self.T = [ 0 for i in range(2 ** L)]
        if seq == None:
            self.seq = [self.gen.generate() for i in range(n)]
        else:
            self.seq = seq
        self.c = 0.7 - 0.8 / self.L + (4 + 32 / self.L) * (self.K ** (-3 / L)) / 15
        self.expectedValue = (self.info[self.L])[0]
        self.variance = (self.info[self.L])[1]
        self.sigma = self.c * (self.variance / self.K) ** 0.5
        
    def seqToInt(self, seq):
        s = ""
        for b in seq:
            s = s + str(b)
        return int(s, 2)

    def getBlockValue(self, i):
        return self.seqToInt(self.seq[(i - 1) * self.L : i * self.L ])

    def test(self):
        for i in range(self.Q):
            self.T[self.getBlockValue(i + 1)] = i + 1
        sum = 0.0
        for i in range(self.Q + 1, self.K + 1):
            sum += math.log2(i - self.T[self.getBlockValue(i)])
            self.T[self.getBlockValue(i)] = i
        fn = sum / self.K
        PValue = math.erfc(abs((fn - self.expectedValue) / (self.sigma * 2 ** 0.5)))
        return PValue