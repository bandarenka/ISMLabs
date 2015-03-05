import LFSR, A5Over1

g1 = LFSR.LSFR([19, 18, 17, 14], 2**16 + 13987, 8)
g2 = LFSR.LSFR([22, 21], 2**21 + 11187, 10)
g3 = LFSR.LSFR([23, 22, 21, 8], 2**13 + 13987, 10)

a5 = A5Over1.AFiveOverOne(g1, g2, g3)
out = []
for i in range(300):
    out.append(a5.generate())
print(out)
