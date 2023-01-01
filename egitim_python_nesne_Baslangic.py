#%%
a=5
print(a)

#%% Classes

class employee:
    #attribute
    #behaviour
    pass

employee1 = employee()


#%% Attribute(özellikleri)

class futbolcu:
    
    futbol_club = "Barcelona"
    age = 30
    
f1=futbolcu()

#%% Methods

class kare(object):
    
    edge=5 #meter
    area=0
    def arean(self):
        self.area = self.edge*self.edge
        print(self.area)
    
k1 = kare()

print(k1.arean())

#%% initializer or constructor methods


class Animal():
    
    def __init__(self,genus,age):
        self.genus=genus
        self.age=age
    
        
    def ageage(self):
        
        return self.age

a1 = Animal("Dog",4)
a2 = Animal("Zebra", 10)
a3= Animal("Bird", 5)


print(a1.ageage())






