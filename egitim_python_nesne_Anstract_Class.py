from abc import ABC, abstractmethod

class abstractclass(ABC): #abstract (Super) class

    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self): pass

    def normalmethod(self): pass



class Bird(abstractclass): #Sub class
    def __init__(self):
        print("Bird")

    def walk(self):
        print("Walk")
    def run(self):
        print("Run")
    def ornek(self):
        print("ornek")  

a1 = Bird()
a1.walk()
a1.ornek()


