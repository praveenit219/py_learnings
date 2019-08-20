
def add(x,y):
    return x+y

def add_sub(x,y):
    return x+y, x-y, x*y, x%y, x/y

result = add(5,6)
print(result)

r1,r2,r3,r4,r5 = add_sub(4,2)
print(r1,r2,r3,r4,r5)