#1.
#Avand lista
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

#Folositi un for ca sa iterati prin toata lista si sa afisati ‘Masina mea preferata este x’
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(0,len(masini)):
    print(f'masina mea preferata este {masini[i]}')

#Faceti acelasi lucru cu un for each
for i in masini:
    print(f'Masina mea preferata este {i}')

#Faceti acelasi lucru cu un while
var = 0
while var<len(masini):
    print(f'Masina mea preferata este {masini[var]}')
    var +=1

#2.
#Aceeasi lista
#Folositi un for
#In for
#   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
#Printati varianta finala a listei

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range (len(masini)):
    if  i!=0 and i!=len(masini)-1:
        masini[i] = masini[i].upper
print(masini)

#3.
#Aceeasi lista,
#Vine un cumparator care doreste sa cumpere un Mercedes
#Iterati prin ea prin for each
#Daca masina e mercedes (if)
#   Printam ‘am gasit masina dorita de dvs’
#   Iesim din ciclu folosind un cuvant cheie care face acest lucru
#Altfel
#   Printam Am gasit masina X. Mai cautam

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina =='Mercedes':
        print('Am gasit masina dorita de dvs')
        break
    print(f'Am gasit masina {masina} . Mai cautam')


#4.
#Aceasi lista
#Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
#Daca masina e Trabant sau Lastun
#   Folositi un cuvant cheie care sa dea skip la ce urmeaza
#Printati S-ar putea sa va placa masina x

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina =='Trabant' or masina=='Lastun':
        continue
    print(f's-ar putea sa va placa masina {masina}')


#5.
#Modernizati parcul de masini
#Creati o lista goala, masini_vechi
#Iterati prin masini
#Cand gasiti Lastun sau Trabant:
#Salvati aceste masini in masini_vechi
#Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
#Printati Modele vechi: x
#Modele noi: x

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fat', 'Trabant', 'Opel']
masini_vechi=[]

for i in range(len(masini)):
    masina = masini[i]
    if masina == 'Lastun' or masina =='Trabant':
        masini_vechi.append(masini)
        masini[i]='Tesla'
print(masini)
print(masini_vechi)


'''
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
Iterati prin lista
'''

pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000 }

for key, value in pret_masini.items():
    print(key, ' : ', value)
for key, value in pret_masini.items():
    if value <=15000:
        print(f'Printati Pentru un buget de sub 15000 euro puteti alege {key}')


'''Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
for numar in numere:
    if numar == 3:
        count = count + 1
print(count)


#8.
#Aceeasi lista
#Iterati prin ea
#Calculati si afisati suma numerelor
#(nu aveti voie sa folositi sum)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

print(f'Suma numerelor din lista este: {sum(numere)}')

sum = 0
for i in range (len(numere)):
    sum = sum + numere[i]
print(f'Suma numerelor din lista este: {sum}')

x = 0
sum2 =0
while x < len(numere):
    sum2 = sum2 + numere[x]
    x +=1
print(f'Suma numerelor din lista este: {sum2}')

#9.
#Aceeasi lista
#Iterati prin ea
#Afisati cel mai mare numar
#(nu aveti voie sa folositi max)

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(f'Valoarea maximă din listă este: {numere [-1]}')
print(f'Valoarea maximă din listă este: {max(numere)}')

#10.
#Aceeasi lista
#Iterati prin ea
#Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
#Ex: daca e 3, sa devina -3
#Afisati noua lista

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(len(numere)):
    if numere[i] < 0:
        numere[i] = 4
print(f'Lista fara numere negative: {numere}')

#varianta 2, pentru a printa numarul negativ
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for num in numere:
    if num < 0:
        print(f'Numerele negative din lista: {num}')

#varianta 3, numere neagtive diferite
numere = [6, -356, 52, 756, 31, -93, 33, 31, 123, 230, -4,-12 ,-8, -9, 3, -257, -346]
numere2 = [element for element in numere if element >= 0]
print("Lista fara numere negative : " + str(numere2))

#varianta 4, cu functia 'FILTER'
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere3 = list(filter(lambda x : x > 0 , numere)) #primul x-argumentul, al doilea x este expresia evaluata
print("Lista fara numere negative : " + str(numere2))

#11.
#alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#numere_pare = []
#numere_impare = []
#numere_pozitive = []
#numere_negative = []
#Iterati prin lista alte_numere
#Populati corect celelalte liste
#Afisati cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

numere_pare = [element for element in alte_numere if element % 2 == 0]
print(f'Numerele pare sunt: {numere_pare}')

numere_impare = [element for element in alte_numere if element % 2 != 0]
print(f'Numerele pare sunt: {numere_impare}')

numere_pozitive = [element for element in alte_numere if element > 0]
print(f'Numerele pare sunt: {numere_pozitive}')

numere_negative = [element for element in alte_numere if element < 0]
print(f'Numerele pare sunt: {numere_negative}')

'''
for num in alte_numere:
    if num % 2 == 0:
        print(f'{num}', end =', ') # ca sa afisam numerele, NU in lista
'''

#12.
#Aceeasi lista
#Ordonati crescator lista fara sa folositi sort
#Va puteti inspira vizual de aici

 #Metoda 1
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for i in range(len(alte_numere)):
   for j in range(i+1,len(alte_numere)):
     if alte_numere[i] > alte_numere[j]:
       alte_numere[i], alte_numere[j]=alte_numere[j],alte_numere[i]
print(f'Lista sortata: {alte_numere}')

# Metoda 2
alte_numere =[-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
lista_sortata = []

while alte_numere:
    min = alte_numere[0]
    for i in alte_numere:
        if i < min:
            min = i
    lista_sortata.append(min)
    alte_numere.remove(min)
print(f'Lista noua : {lista_sortata}')
