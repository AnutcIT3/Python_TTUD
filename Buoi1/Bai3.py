from math import gcd
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
        self.rutgon()
    def rutgon(self):
        UCLN = gcd(self.tu,self.mau)
        self.tu //= UCLN
        self.mau //= UCLN
    def cong(self,PS):
        tu = self.tu*PS.mau+self.mau*PS.tu
        mau = self.mau*PS.mau
        return PhanSo(tu,mau)
    def tru(self,PS):
        tu = self.tu*PS.mau-self.mau*PS.tu
        mau = self.mau*PS.mau
        return PhanSo(tu,mau)
    def nhan(self,PS):
        tu = self.tu*PS.tu
        mau = self.mau*PS.mau
        return PhanSo(tu,mau)
    def chia(self,PS):
        tu = self.tu*PS.mau
        mau = self.mau*PS.tu
        return PhanSo(tu,mau)
    def __str__(self):
        if self.mau == 1:
            return str(self.tu)
        return str(f"{self.tu}/{self.mau}")

    

ps1 = PhanSo(1,2)
ps2 = PhanSo(3,4)
print(ps1.cong(ps2))
print(ps1.tru(ps2))
print(ps1.nhan(ps2))
print(ps1.chia(ps2))

        
    
        