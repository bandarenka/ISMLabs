class SelfShrinked:
    def __init__(self, lsfr):
        self.lsfr = lsfr

    def generate(self):
        first = self.lsfr.generate()
        second = self.lsfr.generate()
        if first == 1 and second == 0:
            return 0
        elif first == 1 and second == 1:
            return 1
        else:
            return self.generate()