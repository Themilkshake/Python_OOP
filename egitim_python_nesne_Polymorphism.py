
class Calisan():       #Super class
    def maasartisi(self):
        artis_degeri= 0.3
        sonuc = 100 + 100*artis_degeri
        return sonuc
        


class Bilgisayar_Muhendisi(Calisan):  #Sub class
    def toString(self):
        return "Bilgisayar Mühendisi"
        
    def maasartisi(self):
        artis_degeri= 0.5
        sonuc = 100 + 100*artis_degeri
        return sonuc
    
class Elektrik_Muhendisi(Calisan):
    def toString(self):
        return "Elektrik Elektronik Mühendisi"
        
    def maasartisi(self):
        artis_degeri= 0.2
        sonuc = 100 + 100*artis_degeri
        return sonuc


BM1 = Bilgisayar_Muhendisi()
EEM1= Elektrik_Muhendisi()




for i in (BM1,EEM1):
    print(i.toString(),": ",i.maasartisi())



