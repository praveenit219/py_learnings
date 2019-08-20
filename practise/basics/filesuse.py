f = open('MyData.txt','r')

print(f)
#print(f.readline(),end='')
#print(f.readline(2))

f1 = open('abc.txt','a')
#f1.write('laptop')

for data in f:
    print(data) 
    f1.write(data)


#for binary files
f = open('pheonix.jpg', 'rb') # we cannot use same for binary files use rb instead of r

#copy files by reading 
f1 = open('ph_copy.jpg', 'wb')
for i in f:
    f1.write(i)
