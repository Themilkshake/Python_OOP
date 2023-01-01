# Calculator Project

class cal():
    
    def __init__(self,a,b):
        
        self.a=a
        self.b=b
    
    def top(self):
        topsonuc= self.a + self.b
        return topsonuc
    
    def cık(self):
        if (self.a>=self.b):
            cıksonuc= self.a - self.b
        elif(self.a<self.b):
            cıksonuc = self.b - self.a
        return cıksonuc
    
    
    def carp(self):
        carpsonuc=self.a*self.b
        return carpsonuc


a= int(input("1. değeri giriniz: "))
b= int(input("2. değeri giriniz: "))

c1=cal(a, b)



while(True):
    k = input("Hangi işlemi yaptırmak istiyorsunuz? (toplama, çıkarma, çarpma): ")
    if (k == "toplama"):
        print(c1.top())
        break
    elif (k=="çıkarma"):
        print(c1.cık())
        break
    elif (k=="çarpma"):
        print(c1.carp())
        break
    else:
        print("Lütfen tekrar giriniz.")




