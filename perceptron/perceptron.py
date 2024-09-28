class Perceptron:

    def __init__(self) -> None:
        self.agirlik=[]
        self.girdi=[]
        self.bias=0.4
        self.cikis=0
        self.k=0.1
        pass

    def ekle(self,girdi,agirlik):
        self.agirlik.append(agirlik)
        self.girdi.append(girdi)
    
    def sil(self,index1,index2):
        self.agirlik.pop(index2)
        self.girdi.pop(index1)

    def show(self,index1,index2):
        return self.girdi[index1],self.agirlik[index2]
        
    def baslat(self):
        agirliklar=self.agirlik[0]
        girdiler  =self.girdi[0]
        sonuc=girdiler[0]*agirliklar[0]+girdiler[1]*agirliklar[1]+girdiler[2]*agirliklar[2]+self.bias
        if(sonuc>=0):
            return 1
        else:
            return 0
        
    def egitim(self,istenilen,tahmin,index):
        agirlik=self.agirlik[0]
        girdi  =self.girdi[0]
        iterasyon=0
        sonuc=tahmin
        while(1):
            for i in range(0,3):
                agirlik[i]=agirlik[i]+self.k*(istenilen-sonuc)*girdi[i]
            self.bias=self.bias+self.k*(istenilen-sonuc)
            sonuc=girdi[0]*agirlik[0]+girdi[1]*agirlik[1]+girdi[2]*agirlik[2]+self.bias
            if(sonuc>=0):
                sonuc= 1
            else:
                sonuc= 0
            print("iterasyon={} sonuc= {}  istenilen={}".format(iterasyon,sonuc,istenilen))
            iterasyon=iterasyon+1
            if(sonuc==istenilen):
                break;
        

