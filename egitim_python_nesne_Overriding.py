class Animal():
    def toString(self):
        print("Animal")
        
class Bird(Animal):    
    def toString(self):
        print("Bird")

a1= Animal()
b1= Bird()

a1.toString()
b1.toString()
    
