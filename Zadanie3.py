#Zadanie 3
from math import sqrt

class LiczbaZespolona:
    re=0
    im=0
    
#konstruktor
    def __init__(self,re,im):
        self.re=re
        self.im=im

#gettey i settery dla czêœci rzeczywistej i urojonej
    def get_re(self):
        return self.re

    def set_re(self):
        self.re=re

    def get_im(self):
        return self.im
    
    def set_im(self):
        self.im=im

#metody do dzia³añ na liczbach zespolonych
    def dodaj(self, liczba):
        re=self.re+liczba.re
        im=self.im+liczba.im
        wynik=LiczbaZespolona(re,im)
        return wynik

    def odejmij(self, liczba):
        re=self.re-liczba.re
        im=self.im-liczba.im
        wynik=LiczbaZespolona(re,im)
        return wynik

    def modulo(self):
        re=self.re
        im=self.im
        wynik=sqrt(re**2+im**2)
        return wynik

#wyœwietlanie wyniku w postaci liczby zespolonej
    def drukuj(self):
        print str(self.re)+ "+" + str(self.im)+ "i"

L1=LiczbaZespolona(2,4)
L2=LiczbaZespolona(9,10)

print "liczba L1 + liczba L2 = "
L1.dodaj(L2).drukuj()
print "\n"

print "liczba L1 - liczba L2 = "
L1.odejmij(L2).drukuj()
print "\n"

print "modulo z liczby L1 = "
print L1.modulo()
print "\n"

print "modulo z liczby L2 = "
print L2.modulo()


        

        
        
    



