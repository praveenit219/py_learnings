#if the class use is only for this outerclass to go for inner class

class Student:

	def __init__(self, name, rollno):
		self.name = name
		self.rollno = rollno
		self.lap = self.Laptop() #initialise inner class inside outer calss init

	def show(self):
		print(self.name, self.rollno)
		self.lap.show() #access inner class methods in outclass using the lap

	class Laptop:
		def __init__(self):
			self.brand = 'HP'
			self.cpu = 'i5'
			self.ram = 8

		def show(self):
			print(self.brand, self.cpu, self.ram)


s1 = Student('Nani', 30)
s2 = Student('Che', 32)

print(s2.name, s2.rollno)
s1.show()

lap1 = s1.lap
print(id(lap1))

print(lap1.brand, lap1.cpu, lap1.ram)

lap2 = s2.lap
print(id(lap2))

lap1 = Student.Laptop() #outerclass  inner class
lap1.show()