

#global
a = 10
print(id(a))

def something():
    #local
    a = 15
    print("in func", a)

def useGlobalInLocal():
    print("global inside func", a)

def useGlobalInLocalwithsameVar():
    global a 
    a = 20
    print(" local inside func", a)
   # a = 7 
    print("global inside fun with same name", a  )

def usingGlobals():
    a = 9
    print(id(a))
    x = globals()['a']
    print(id(x))
    print('in func to use globals - what is local a =', a)
    print('in func to use globals with x - what is global a =', x)
    x = globals()['a'] = 11
    print(id(x))
    print('after changing globals - what is global a = ', x)
    print('after changing globals - what is local a = ', a)


usingGlobals()
print(id(a))
print("out func", a)    
#useGlobalInLocalwithsameVar()
#useGlobalInLocal()
#something()


