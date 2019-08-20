
from functools import reduce
#map
#reduce

def is_even(n):
    return n%2 == 0

nums = [3,2,6,8,4,6,2,9]

#filter with defined function
evens =  list(filter(is_even,nums))
print(evens)

#filter with lambda
evens = list(filter(lambda n : n%2 ==0, nums))
print(evens)

def update(n):
    return n*2

#map with defined function
doubles = list(map(update, evens))
print(doubles)

#map with lambda
doubles = list(map(lambda n : n*2, evens))
print(doubles)


def add_all(a,b):
    return a+b

#reduce have to import from fun
sum = reduce(add_all, doubles)
print(sum)

#reduce with lambda
sum = reduce(lambda a,b : a+b, doubles)
print(sum)