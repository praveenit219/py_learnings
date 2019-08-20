#make sure elements are sorted
#l, u. find the mid using l+u/2 (int value)
#compare mid with the element to search
#if not found, find the value is less than searching value, go to left and change left bound to mid do again 2,3 steps
# if the value is greater than seraching value, go to right and change wih right boudnto mid and do again 2,3 steps

pos = -1

def search(list, n):
    l = 0
    u = len(list)-1
    
    while l <= u:
        m = (l+u)//2
        if list[m] == n:
            globals()['pos'] = m
            return True
        else:
            if list[m] < n:
                l = m+1
            else:
                u = m-1
    return False


list = [4,7,8,12,45,99,102,702,10987,56666]
n = 10

if search(list, n):
    print('found at', pos+1)
else:
    print('not found')


