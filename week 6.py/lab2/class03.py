class Person:
    def __init__(self):
        self.A="james"
        self.__B="james bond"
    def printname(self):
        print(self.A)
        print(self.__B)
p=Person()
p.A
p.__B

p.printname()