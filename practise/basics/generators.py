#generator will give you iterator
#by using yield fro a funtion it will give generator, then we can use iterator by using next to check values

def topten():
    yield 5
    #return 5
    yield 4
    yield 3
    yield 2

values = topten()
print(values.__next__())
#at this moment return 5 and yield 5 return same number. return will terminate your function but yield is not 
print(values.__next__())

for i in values:
    print(i)

def toptenPerfectSquares():
    n = 1
    while n <= 10:
        sq = n*n
        yield sq
        n = n+1

values = toptenPerfectSquares()
print('topten perfect squares')
for i in values:
    print(i)