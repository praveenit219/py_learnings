
def add(a,b):
    c = a+b
    print(c)


add(5,6)

#position

def person(name, age):
    print(name)
    print(age)

print('praveen', 30)
print(30, 'praveen')


#keyword

person(age=40,name='praveen')
person(name='nani', age=30)

#default

def person(name, age=18):
    print(name)
    print(age)

person('nani')
person('nani',45)
person(age=41,name='nani')

#variable length

#def sum(a,*b):
def sum(*b):
    c = 0
    for i in b:
        c = c+i
        print(c)    

sum(5,6)
sum(5,6,7)
