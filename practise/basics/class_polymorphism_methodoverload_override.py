#mehod overloading -> two methods same name but different params. pythond doesn't haev this concept
# example Student: class -> def average(c), def average(c,b) 
class Student:
    def __init__(self, m1, m2 ):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s


s1 = Student(58, 69)
print(s1.sum(5))
print(s1.sum(5,9))
print(s1.sum(5,9,6)) # this will not work as TypeError: sum() takes 3 positional arguments but 4 were given. in other languages we create another method to match the params. but here we an do another variable in same method. but that gives error we can solve this bypassing some deafult value as "None". using None and same method for differnet parameters is called method overladign


#method override -> two methods same name same number of params. pythong possible but not in same class but using inheritence

class A:
    def show(self):
        print('in A show')

class B(A):
    pass

class C(A):
    def show(self):
        print('in C show')

a1 = A()
a1.show()

b1 = B()
b1.show()

a1 = C()
a1.show() #method overriding using inheritence, if you have method available its prioritised then suepr class 