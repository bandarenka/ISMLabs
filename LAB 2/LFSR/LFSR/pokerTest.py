class PokerTest:
    def __init__(self, seq, m):
        self.seq = seq
        self.n = len(seq)
        self.m = m
        self.k = self.n // m
        self.N = [0 for i in range(2 ** m)]
    def seqToInt(self, seq):
        s = ""
        for b in seq:
            s = s + str(b)
        return int(s, 2)

    def getBlockValue(self, i):
        return self.seqToInt(self.seq[i * self.m : (i + 1) * self.m])

    def test(self):
        for i in range(self.k):
            self.N[self.getBlockValue(i)] = self.N[self.getBlockValue(i)] + 1
        return self.calculateStatistic()

    def calculateStatistic(self):
        sum = 0
        for i in range(2 ** self.m):
            sum += self.N[i] ** 2 
        return 2 ** self.m * sum / self.k - self.k