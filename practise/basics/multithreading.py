from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(500):
            print('Hello')
            


class Hi(Thread):
    def run(self):
        for i in range(500): 
            print('Hi')
            

t1 = Hello()    
t2 = Hi() 
 
#t1.run()
#t2.run()
 
t1.start() #t1 thread
t2.start() #t2 thread
 
t1.join()
t2.join()

print('bye') #main thread complete here. if you want main thread to wait until other threads complete then use join for other threads