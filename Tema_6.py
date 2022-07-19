#Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei
#1.
#Clasa Cerc
#Atribute: raza, culoare
#Constructor pt ambele atribute
#Metode:
#descrie_cerc() - va PRINTA culoarea si raza
#aria() - va RETURNA aria
#diametru()
#circumferinta()

class Cerc:
    #atribute
    raza = None
    culoare = None
    #constructor
    def __init__(self, raza, culoare):
        self.raza=raza
        self.culoare=culoare
        #metode
    def descriere_cerc(self):
        print(f'Cercul are culoare {self.culoare} si dimensiunea razei este de {self.raza} cm')

    def aria(self):
        aria = 3.14 * self.raza
        print(f'Aria cercului este de {aria} cm')

    def diametru(self):
        diametru = 2 * self.raza
        print(f'Diametrul cercului este de {diametru} cm')

    def circumferinta(self):
        circumferinta = 2 * 3.14 * self.raza
        print(f'Circumferinta cercului este de {circumferinta} cm')

cerc_1 = Cerc(3, 'mov')
cerc_1.descriere_cerc()
cerc_1.aria()
cerc_1.diametru()
cerc_1.circumferinta()

print(end='\n')  #pentru spatiu

cerc_2 = Cerc(7.27, 'portocaliu')
cerc_2.descriere_cerc()
cerc_2.aria()
cerc_2.diametru()
cerc_2.circumferinta()

print(end='\n')

cerc_3 = Cerc(19.48, 'albastru')
cerc_3.descriere_cerc()
cerc_3.aria()
cerc_3.diametru()
cerc_3.circumferinta()

print(end='\n')
print(end='\n')

class Dreptunghi:
    #atribute
    lungime = None
    latime = None
    culoare = None

    #constructor
    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare =culoare

    #metode
    def descriere(self):
        print(f'Dreptunghiul are lungimea de  {self.lungime} cm, latimea de {self.latime} si culoarea acestiua este {self.culoare}')

    def aria(self):
        aria = self.lungime * self.latime
        print(f'Aria dreptunghiului este de {aria} cm')

    def perimetrul(self):
        perimetru = (2 * self.lungime) + (2 * self.latime)
        print(f'Perimetrul dreptunghiului este de {perimetru} cm')

    def schimba_culoarea(self, culoare_noua):
        self.culoare = culoare_noua

dreptunghi_1 = Dreptunghi(8,6,'alb')
dreptunghi_1.descriere()
dreptunghi_1.aria()
dreptunghi_1.perimetrul()
dreptunghi_1.schimba_culoarea('mov')

print(end='\n')

class Angajat:
    #atribute
    nume = None
    prenume = None
    salariu = None

    #constructor

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    #metode

    def descrie(self):
        print(f'Numele angajatului este {self.nume} {self.prenume} iar salariul acestiu este de {self.salariu} lei')

    def nume_complet(self):
        print(f'Numele complet al angajatului este {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul angajatului este {self.salariu}')

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f'Salariu anual al angajatului este {salariu_anual}')

    def marire_salariu(self, procent):
        self.salariu = procent
        print(f'Salariu a fost marit cu {procent}%')


angajat_1 = Angajat('Pop', 'Alex', 3500)
angajat_1.descrie()
angajat_1.nume_complet()
angajat_1.salariu_lunar()
angajat_1.salariu_anual()
angajat_1.marire_salariu(12)
print(end='\n')

class Cont:
    #atribute
    iban = None
    titualr_cont = None
    sold = None

    #constructor
    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titualr_cont = titular_cont
        self.sold = sold

    #metode
    def afisare_sold(self):
        print(f'Titularul {self.titualr_cont} are in contul {self.iban} suma de {self.sold}')

    def debitare_cont(self, suma_debitare):
        self.sold = suma_debitare
        print(f'Titularul {self.titualr_cont} are suma de {self.sold},  debit')

    def creditare_cont(self, suma_creditare):
        self.sold = suma_creditare
        print(f'Titularul {self.titualr_cont} are suma de {self.sold}, credit')

cont_1 = Cont('RO1234', 'Pop Eleonora', 1230.52)
cont_1.afisare_sold()
cont_1.debitare_cont(1000)
cont_1.creditare_cont(657.45)
print(end='\n')

class Factura:
    #atribute
    seria = 'FDB'
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    #constructor
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    #metode
    def schimba_cantitatea(self, cantitate_noua):
        self.cantitate = cantitate_noua
        print(f'Cantitatea noua este {self.cantitate}')

    def schimba_pretul(self, pret_nou):
        self.pret = pret_nou
        print(f'Pretul nou este {self.pret}')

    def schimba_nume_produs(self, nume_nou):
        self.nume_produs = nume_nou
        print(f'Noul nume este {self.nume_produs}')

factura_1 = Factura(123, 'Electrica', 322, 6.02)
print(f'Factura seria {seria} numar {self.numar}')

from datetime import date
today = date.today()
print('Data de azi este', today)

#revizuire tema 6



















