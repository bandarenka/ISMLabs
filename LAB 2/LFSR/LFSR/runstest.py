import math
class RunsTest:
    def __init__(self, seq):
        self.seq = seq
        self.n = len(seq)
        self.pi = sum(seq) / self.n
        self.totalRuns()
        self.tau = 2 / self.n ** 0.5

    def totalRuns(self):
        self.Vn = 1

        for i in range(1, self.n):
            if self.seq[i] != self.seq[i - 1] :
                self.Vn += 1
        if sum(self.seq) == self.n or sum(self.seq) == 0:
            self.Vn = 1

    def test(self):
        if abs(self.pi - 0.5) >= self.tau:
            return 0
        PValue = math.erfc(abs(self.Vn - 2 * self.n * self.pi * (1 - self.pi)) \
            / (2 * self.pi * (1 - self.pi) * (2 * self.n) ** 0.5 ))
        return PValue
       
    def frequencyTest(self):
        s = abs(len(self.seq) - 2 *sum(self.seq))
        s = s / ((len(self.seq)) ** 0.5)
        s = s / (2 ** 0.5)
        return math.erfc(s)

r = RunsTest([1, 0, 0,1,1,0,1,0,1,1])
r.totalRuns()
print(r.test())