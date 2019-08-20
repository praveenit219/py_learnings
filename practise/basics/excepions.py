a = 5
b = 0

try:
    print('open resource')
    print(a/b)
    k = int(input('enter a number'))
    print(k)

except ZeroDivisionError as e:
    print('cannot be divided by "0"')
except ValueError as e:
    print('invalid input')
except Exception as e:
    print('something went wrong...')


finally:
    print('close resource')
