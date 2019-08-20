def update(x):
    print(id(x))
    x = 8    
    print(id(x))
    print("x ",x)

def updatelist(lst):
    print(id(lst))
    lst[1] = 35
    print(id(lst))
    print("x in lst ", lst)


lst = [10,20,30]
print(id(lst))
updatelist(lst)
print("lst ", lst)


a = 10
print(id(a))
update(a)
print("a ",a)