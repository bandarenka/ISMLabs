import SelfShrinkedGen, LFSR, MauerTest, lab1, pokerTest, runstest
taps = (32, 30, 27, 23, 19, 17, 13, 11, 7, 5)
start = 0b01011001
g = LFSR.LSFR(taps, start)
sg = SelfShrinkedGen.SelfShrinked(g)
out = []
#while len(out) < 60000:
#    out.append(sg.generate())
#print(out)

#mt = MauerTest.MauerTest(sg, 387840, 6, 640)
#print(mt.test())

y = lab1.Generator(11,37,1250,5)
seq = lab1.discrete(y,60000,1)
#mt = MauerTest.MauerTest(y , 20000, 6, 640, seq)
#print(mt.test())
seq0 = [1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1]
seq = list(seq0)
seq.extend(seq0)
seq.extend(seq0)
seq.extend(seq0)
#pt = pokerTest.PokerTest(out, 10)

#print(pt.test())

#rt = runstest.RunsTest(out)
#print(rt.test())

rt = runstest.RunsTest(seq)
print(rt.test())