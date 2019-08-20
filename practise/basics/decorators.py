
def div(a,b):
    return a/b

print(div(2,4))


#decorator to make sure the sequene of arguements passed here should be like which ever is bigger should be passed to a and other b so we always get int then floating

def div(a,b):
    if a<b:
        a,b = b,a
    return a/b
print(div(2,4))

#what if we dont have div in our scope, what if it is third party libraries we cannot edit.

def div(a,b):
    return a/b


def smart_div(func):

    def inn_div(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inn_div

div = smart_div(div)
print(div(2,4))