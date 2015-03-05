
class LSFR:
    def __init__(self, taps, start, synchBitNumber = None):
        self.n = max(taps)
        self.taps = taps
        self.curr = start
        self.synchBitNumber = synchBitNumber

    def generate(self):
        xor = 0
        for i in self.taps:
            curr_bit = ((2 ** (i - 1)) & self.curr) >> (i - 1)
            xor = xor ^ curr_bit
        out = 0b1 & self.curr
        self.curr = self.curr >> 1
        self.curr = (xor * (2 ** (self.n - 1))) | self.curr
        return out

    def getSynchBit(self):
        return ((2 ** self.synchBitNumber) & self.curr) >> self.synchBitNumber