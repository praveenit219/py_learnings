#duckTyping only cares on that method available but it doesn't care on what it is. here ide of type anything but Laptop doesn't care it only sees the execute methods here from the object we pass in code method.

class PyCharm:
    def execute(self):
        print('compiling')
        print('run')

class VSC:
    def execute(self):
        print('spellCheck')
        print('format')
        print('compiling')
        print('run')


class Laptop:
    def code(self,ide):
        ide.execute()


ide = PyCharm()
ide1 = VSC()

lap1 = Laptop()
lap1.code(ide)

lap1.code(ide1)