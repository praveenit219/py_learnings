#singlelevel  multilevel
# A->B         A->B->C
#Multiple
#   A ->
#        |-> C  
#   B ->

class A:
    """description of class"""
    def feature1(self):
        print("Feature1 working A")

    def feature2(self):
        print("Feature2 working A")


class B(A):
    def feature3(self):
        print("Feature3 working B")

    def feature4(self):
        print("Feature4 working B")



class C(B):
    def feature5(self):
        print("Featur5 working c")

    def feature6(self):
        print("Feature6 working c")


class ex1:
    def exFeautre1(self):
        print("exFeautre1 ex1")

class ex2:
    def exFeautre2(self):
        print("exFeautre2 ex2")

class D(ex1,ex2):
    def feature7(self):
        print("Featur7 working D")


a1 = A()
a1.feature1()
a1.feature2()

b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
c1.feature6()

d1 = D()
d1.feature7()
d1.exFeautre1()
d1.exFeautre2()