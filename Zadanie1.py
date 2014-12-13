#Zadanie 1

plik_wejscie=open("statystyki.txt","r")
plik_wyjscie=open("statystyki2.txt","w")

for linia in plik_wejscie:
    linijki=linia.split(" ")
#print linijki
  
y=[]
for i in linijki:
    y.append(linijki.count(i))
#print y


z=[]
for j in range(0,len(y)):
    z.append(linijki[j]+': '+str(y[j]))
#print z

#Tworzê zbiór z listy, gdy¿ zbiór zawiera wartoœci unikalne, wiêc s³owa nie bêd¹ siê powtarzaæ
z2=set(z)

plik_wyjscie.writelines([linie+"\n" for linie in z2])
plik_wyjscie.close()
    



