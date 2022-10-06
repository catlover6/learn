class Polynomial:
    def __init__(self):
        self.poly = []

    def degree(self):
        return len(self.poly)-1

    def evaluate(self, num):
        cnt = 0
        for i in range(1,len(self.poly)):
            cnt += num ** (i)*self.poly[i]
        cnt+= self.poly[0]
        return cnt

    def add(self, polyb):
        listc = []
        if len(self.poly) >= len(polyb):
            for i in range(len(polyb)):
                listc.append(self.poly[i] + polyb[i])
            for i in range(len(polyb), len(self.poly)):
                listc.append(self.poly[i])
        else:
            for i in range(len(self.poly)):
                listc.append(self.poly[i] + polyb[i])
            for i in range(len(self.poly), len(polyb)):
                listc.append(polyb[i])
        return listc

    def inverse(self):
        listc = []
        for i in range(len(self.poly)):
            listc.append(self.poly[i]*-1)
        return listc

    def display(self, msg):
        print(msg,end="")
        for i in range(len(self.poly)-1):
            print(self.poly[len(self.poly)-1-i],"x^",len(self.poly)-1-i,end = " + ")
        print(self.poly[0])

    def read(self):
        print("다항식의 최고 차수를 입력하시오")
        tmp= int(input())
        for i in range(tmp):
            print("x^",i,"의 계수:")
            tmp1 = int(input())
            self.poly.append(tmp1)

a = Polynomial()
a.read()

b = Polynomial()
b.read()

a.display("a(x) = ")
b.display("b(x) = ")

c= Polynomial()
c.poly = a.add(b.poly)
c.display("c(x) = ")
print("a의 차수",a.degree())
print("c에 2를 대입한 결과",c.evaluate(2))
c.display("c(x) = ")
print(c.inverse())
