# Kalıtım, Miras

#Parent (super class)
class Animal():
    def __init__(self):
        print("Hayvan yaratıldı.")
        
    def Walk(self):
        print("animal walk")
        
    def Kosma(self):
        print("animal run.")        
        
        
#Child (sub class)

class Monkey(Animal):
    def __init__(self):
        super().__init__() #<--- Parent class'ındaki init metodunun içeriğini Child'a aktarıyor.
        print("Maymun yaratıldı.")
        
        
    def Climb(self):
        print("Maymun zıplayabiliyor.")

monkey1 = Monkey()


class Cat(Animal):
    def __init__(self):
        super().__init__()
    
    def kuyrukhareketi(self):
        print("Kuyruk hareketi")
        

cat1 = Cat()

cat1.kuyrukhareketi()



               



