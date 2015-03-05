import tkinter

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


def initialMoment(list, k):
    s = set(list)
    sum = 0.0
    p = 1 / len(s)
    for i in s:
        sum += p * i ** k
    return sum

def centralMoment(list, k):
    s = set(list)
    sum = 0.0
    E = initialMoment(list, 1)
    p = 1 / len(s)
    for i in s:
        sum += p * (i - E) ** k
    return sum

x = Generator(67, 45, 101, 0)
y = Generator(11,37,1250,5)

mc64 = McLarenGen(x, y, 64)
mc128 = McLarenGen(x, y, 128)

f = open("out.txt", 'w')

def writeListToFile(f, list, number,message):
    f.write(message)
    f.write(str(number))
    f.write("\n")
    f.write(str(list))
    f.write("\n")
    f.write("\n")

def writeBlockToFile(f, containerOfLists, message):
     for i in containerOfLists:
         writeListToFile(f, i, containerOfLists.index(i) + 1, message)

def writeInitMomentToFile(f):
    for i in range(1, 6):
        f.write("Init moment generator 1, k =" + str(i) + ": " )
        f.write(str(initialMoment(continuous(x, x.M), i) ))
        f.write("\n")
    for i in range(1, 6):
        f.write("Init moment generator 2, k =" + str(i) + ": " )
        f.write(str(initialMoment(continuous(y, y.M), i) ))
        f.write("\n")
    for i in range(1, 6):
        f.write("Init moment generator 3, k =" + str(i) + ": " )
        f.write(str(initialMoment(continuous(mc64, mc64.M), i)) )
        f.write("\n")
    for i in range(1, 6):
        f.write("Init moment generator 4, k =" + str(i) + ": " )
        f.write(str(initialMoment(continuous(mc128, mc128.M), i) ))
        f.write("\n")
    f.write("\n")

def writeCentralMomentToFile(f):
    for i in range(1, 6):
        f.write("Central moment generator 1, k =" + str(i) + ": " )
        f.write(str(centralMoment(continuous(x, x.M), i) ))
        f.write("\n")
    for i in range(1, 6):
        f.write("Central moment generator 2, k =" + str(i) + ": " )
        f.write(str(centralMoment(continuous(y, y.M), i) ))
        f.write("\n")
    for i in range(1, 6):
        f.write("Central moment generator 3, k =" + str(i) + ": " )
        f.write(str(centralMoment(continuous(mc64, mc64.M), i)) )
        f.write("\n")
    for i in range(1, 6):
        f.write("Central moment generator 4, k =" + str(i) + ": " )
        f.write(str(centralMoment(continuous(mc128, mc128.M), i) ))
        f.write("\n")
    f.write("\n")
 
def writeDiscrete(f):

    for l in range(1,6):

        f.write("Init moments" + str(l))
        f.write("\n")
        for i in range(1, 4):
            f.write(str(initialMoment(discrete(y, y.M, i), l)))
            f.write("\n")

        f.write("central moments" + str(l))
        f.write("\n")
        for i in range(1, 4):
            f.write(str(centralMoment(discrete(y, y.M, i), l)))
            f.write("\n")

seq = []
seq.append(x.generateList(x.M))
seq.append(y.generateList(y.M))
seq.append(mc64.generateList(mc64.M))
seq.append(mc128.generateList(mc128.M))

writeBlockToFile(f, seq, "Generator ")
initConMoments = []
initDiscrMoments = []
centralConMoments = []
centralDiscrMoments = []

seq.clear()

seq.append(continuous(x, x.M))
seq.append(continuous(y, y.M))
seq.append(continuous(mc64, mc64.M))
seq.append(continuous(mc128, mc128.M))

writeBlockToFile(f, seq, "Continuous ")

for i in range(1,4):
    seq.clear()
    seq.append(discrete(x, x.M, i))
    seq.append(discrete(y, y.M, i))
    seq.append(discrete(mc64, mc64.M, i))
    seq.append(discrete(mc128, mc128.M, i))
    writeBlockToFile(f, seq, "Discrete " + " (N = " + str(i) + ") ")

writeInitMomentToFile(f)
writeCentralMomentToFile(f)

binSeq = []
binSeq .append(discrete(x, x.M, 1))
binSeq .append(discrete(y, y.M, 1))
binSeq .append(discrete(mc64, mc64.M, 1))
binSeq .append(discrete(mc128, mc128.M, 1))

def nistTest(list):
    s = abs(len(list) - 2 *sum(list))
    s = s / ((len(list)) ** 0.5)
    s = s / (2 ** 0.5)
    return s

for i in binSeq:
    print(nistTest(i))

writeDiscrete(f)


f.close()
tk1 = tkinter.Tk()
tk2 = tkinter.Tk()
tk3 = tkinter.Tk()
tk4 = tkinter.Tk()

tk1.title  = "dfghj"

def diagram(canvas, list):
    for p in list:
        x, y = p
        
        x *= 1000
        y *= 1000
        x = int(x)
        y = int(y)
        
        canvas.create_oval((x, y, x + 2, y + 2))

def createPoints(list):
    return [(list[i], list[i+1]) for i in range(0, len(list)-1, 2)]

canvas1 = tkinter.Canvas(tk1, height = 1000, width = 1000)
canvas2 = tkinter.Canvas(tk2)

print (continuous(x, x.M))
diagram(canvas1, createPoints(continuous(mc64, mc64.M)))

canvas1.pack()
canvas2.pack()
tk1.mainloop()
tk2.mainloop()