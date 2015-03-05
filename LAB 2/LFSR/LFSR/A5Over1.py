#import LFSR
class AFiveOverOne:
    def __init__(self, g1, g2, g3):
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3
      
    def majoraty(self):
        x = self.g1.getSynchBit()
        y = self.g2.getSynchBit()
        z = self.g3.getSynchBit()
        return x&y|x&z|y&z

    def generate(self):
        maj = self.majoraty()
        gens = (self.g1, self.g2, self.g3)
        out = []
        for g in gens:
            if maj == g.getSynchBit():
                out.append(g.generate())
        res = 0
        for i in out:
            res ^= i
        # ????????????
        return res
