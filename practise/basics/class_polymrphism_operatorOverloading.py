#magic mehods for a class custom class or pre-defined classes in py for operator overloading
#check all the default methods for a class for those magic methods to overload

a = 5
b = 'world'

#print(a + b ) # will throw TypeError: unsupported operand type(s) for +: 'int' and 'str'

a = 5
b = 6
print(a+b) #behind scenes it uses it calls int class and use add becz of opertaor + and same type int class
print(int.__add__(a,b))
#for strings
a = '5'
b = '6'
print(a+b) # internal it calls str class magic methods __add__ 
print(str.__add__(a,b)) #we call string explicitly instead of print(a+b)


# operator overloading on custom classes
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1+other.m1
        m2 = self.m2+other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):
        s1 = self.m1+self.m2
        s2 = other.m1+other.m2
        if s1>s2:
            return True
        else:
            return False

    def __str__(self):
        return '{}, {}'.format(self.m1, self.m2)


s1 = Student(58,69)
s2 = Student(60,85)

s3 = s1 + s2 # if we dont define what will happen for this type of class, py throw erro TypeError: unsupported operand type(s) for +: 'Student' and 'Student'. 
            #now  we add __add__ method in student class to do specific operation for "+" now s1 + s2 will execute by calling overloaded __add__

print(s3.m1, s3.m2) #now we call s3 for m1 and m2

if s1>s2:
    print('s1 is winnner')
else:
    print('s2 is winner')
    #TypeError: '>' not supported between instances of 'Student' and 'Student'. we should make sure to have a method for comparing two objects on class


a = 9
print(a) # prints value of a

print(s1) # prints address of s1 class not actual value like 'a' above for type class int
            # if we want to print values of s1 instead of address we need to overload str

print(a.__str__())
#defniing __Str__ method to return string of values for a class object can help to print s1 in print function.  internal it calls __str__
print(s1.__str__())

