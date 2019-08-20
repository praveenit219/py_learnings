pos = -1
posfor = -1

#using while to find the value in list and position of it
def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i+1
    return False

#using for to find the value in list and position of it
def search_for(list, n):
    for i in list:
        if i == n:
            globals()['posfor'] = list.index(n)
            return True
    return False


list = [5,8,4,7,6,9,0]
n = 7
if search(list, n):
    print('found at ', pos+1)
else:
    print('not found')

if search_for(list,n):
    print('for found at ', posfor+1)
else:
    print('for not found')
