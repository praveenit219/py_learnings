#static/class variable
#instance/object variables

class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'BMW'


c1 = Car()
c2 = Car()

print(c1.com, c1.mil)
print(c2.com, c2.mil)

c1.mil = 2

print(c1.com, c1.mil)
print(c2.com, c2.mil)


print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)

print(c1.com, c1.mil, Car.wheels)
print(c2.com, c2.mil, Car.wheels)

Car.wheels = 5

print(c1.com, c1.mil, Car.wheels)
print(c2.com, c2.mil, Car.wheels)