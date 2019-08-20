class class_sample:
    """description of class"""
    def config(self):
        print ('i5, 16g, 1TB')

a = '8'
print(type(a))

x = 9
print(type(x))

class_sam_obj = class_sample()
class_sam_obj1 = class_sample()
print(type(class_sam_obj))
class_sam_obj.config()
class_sam_obj1.config()
class_sample.config(class_sam_obj)
class_sample.config(class_sam_obj1)

#self with args in intialisation

class comp:
     def __init__(self,cpu,ram):
        print('init')
        self.cpu = cpu
        self.ram = ram
    
     def config(self):
        print ('config is', self.cpu, self.ram)



compobj1 = comp('amdRyan',8)
compobj1.config()