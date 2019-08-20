#inheritance constructors
#super methods for init
#super methods to call diff methods
#MRO (method resolution order)

class A:
    """description of class"""
    def feature1(self):
        print('feature1 in A')

    def __init__(self):
        print("in A Init")


class B(A):
    """description of class"""
    def __init__(self):
        #to call super class constructor also  then here we use super     
        super().__init__()   #order is not important 
        print("in B Init")
        

    def feature2(self):
        print('feature2 in B')

#a1 = A() #initialise with A  constructor
b1 = B() #intialise  B constructor only, if it is not there then only go to A 
        
#b1.feature1()
#b1.feature2()


class A1:
    """description of class"""
    def feature1(self):
        print('feature1 in A1')

    def featureMRO(self):
        print('featureMRO in A1')

    def __init__(self):
        print("in A1 Init")


class B1:
    """description of class"""
    def __init__(self):
        print("in B1 Init")

    def featureMRO(self):
        print('featureMRO in B1')       

    def feature2(self):
        print('feature2 in B1')


class C(A1,B1):
    def __init__(self):
        super().__init__() 
        """even we inherit both calss to , super only take A1 first. bec of MRO, as A1, B1 -> C meaning it goes left to right it starts inherting"""
        """same MRO goes to methods also. if same methods are inheritec from super classes to sub. then MRO takes left most first and not then right most following order"""
        print('C in init') 

    def feat(self):
        super().feature2() #call super class method using super() in subclass method

c1 = C() #only calls C init 
c1.featureMRO() # calls A1 MRO becz of left to right inheritance of two super classese A1 and B1 to C
c1.feat()