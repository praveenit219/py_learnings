class computer:
    def __init__(self):
        self.name = 'praveen'
        self.age = 31

    def updateVal(self):
        self.age = 31

    def compare(self,other):
        if(self.age == other.age):
            return True
        else:
            return False

c1 = computer()
print(c1.name)

c1.name = 'nani'
print(c1.name)
print(c1.age)

c1.updateVal()
print(c1.age)

c2 = computer()
print(c2.name)
print(c2.age)

if c1.compare(c2):
    print('they are same')
else:
    print('they are not same')