

def fac(n):
    f = 1
    for i in range(1, n+1):        
        f = f*i
    return f


x = 6
result = fac(x)
print(result)

if __name__ == '__main__':
    print(__name__)