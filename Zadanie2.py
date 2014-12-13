#Zadanie 2

plik=open("menu.txt","r")


for linia in plik:
    lista=linia.split(" ")
    #print lista

klucze=lista[::2]
#print klucze

wartosci=lista[1::2]
#print wartosci

klucz_wartosc=zip(klucze, wartosci)
menu=dict(klucz_wartosc)

#print menu

def koszt(zamowienie):
    cena=[]
    for i in zamowienie:
        cena.append(float((menu[i])))
        
    napiwek=0.10*sum(cena)
    wartosc=sum(cena)+napiwek
    
    return wartosc

print "Ca³kowita wartoœæ z³o¿onego zamówienia wynosi: "
print koszt(['zupa_pomidorowa','schabowy'])

        
        
    



