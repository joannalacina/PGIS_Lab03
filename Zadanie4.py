#Zadanie 4


class Budynek:
    
    liczbaKondygnacji=0
    iloscPokoi=0

    def __init__(self,liczbaKondygnacji,iloscPokoi):
        self.liczbaKondygnacji=liczbaKondygnacji
        self.iloscPokoi=iloscPokoi
        
    def get_liczbaKondygnacji(self):
        return self.liczbaKondygnacji

    def set_liczbaKondygnacji(self):
        self.liczbaKondygnacji=liczbaKondygnacji

    def get_iloscPokoi(self):
        return iloscPokoi
    
    def set_iloscPokoi(self):
        self.iloscPokoi=iloscPokoi

    def infObudynku(self):
        print "Budynek posiada " + str(self.liczbaKondygnacji) + " kondygnacji oraz " + str(self.iloscPokoi) + " pokoi"


class Szpital:

    iloscOddzialow=0

    def __init__(self,iloscOddzialow):
        self.iloscOddzialow=iloscOddzialow
        
    def get_iloscOddzialow(self):
        return iloscOddzialow
    
    def set_iloscOddzialow(self):
        self.iloscOddzialow=iloscOddzialow

    def infOszpitalu(self):
        print "Szpital posiada " + str(self.iloscOddzialow) + " oddzialow "
        

class Domek(Budynek):

    def __init__(self,liczbaKondygnacji,iloscPokoi):
        self.liczbaKondygnacji=liczbaKondygnacji
        self.iloscPokoi=iloscPokoi

    def infOdomku(self):
        print "Domek posiada " + str(self.liczbaKondygnacji) + " kondygnacji oraz " + str(self.iloscPokoi) + " pokoi"


class Sanatorium(Budynek, Szpital):

    def __init__(self,liczbaKondygnacji,iloscOddzialow):
        self.liczbaKondygnacji=liczbaKondygnacji
        self.iloscOddzialow=iloscOddzialow

    def infOsanatorium(self):
        print "Sanatorium posiada " + str(self.liczbaKondygnacji) + " kondygnacji oraz " + str(self.iloscOddzialow) + " oddzialow"


budynek=Budynek(10,36)
budynek.infObudynku()

szpital=Szpital(12)
szpital.infOszpitalu()

domek=Domek(2,6)
domek.infOdomku()

sanatorium=Sanatorium(6,12)
sanatorium.infOsanatorium()



    




        

        
        
    



