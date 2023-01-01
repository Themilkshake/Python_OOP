class BankaHesabi():
    
    def __init__(self,name,money,address):
        self.name=name
        self.__money=money
        self.address=address
    
    # get and set
    
    def getMoney(self):
        return self.__money
    
    def setMoney(self,miktar):
        self.__money = miktar


p1= BankaHesabi("Messi", 1000, "Barce")
p2= BankaHesabi("Neymar", 2000,"Paris")


p1.setMoney(5)

print(p1.getMoney())