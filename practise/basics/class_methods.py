#class methods
#instance/object methods
#static methods


class Student:

    school = 'Cambridge'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, newValue):
        self.m1 = newValue

    def info(self):
        return self.school


    def info(cls):
        return cls.school



s1 = Student(34,16,38)
s2 = Student(23,12,34)

print(s1.avg())
print(s2.avg())



print(Student.info())