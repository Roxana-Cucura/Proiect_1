
#1. Declară o listă note_muzicale în care să pui do re mi etc până la do, Afișeaz-o:

note_muzicale= ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
note_muzicale = note_muzicale[::-1] #IMPORTANT!!!
print(note_muzicale)

#2. De câte ori apare ‘do’?
print(note_muzicale.count('do'))

#3. Având 2 liste, [3, 1, 0, 2] și [6, 5, 4].
#   Găseste 2 variante să le unești într-o singură listă.

#METODA 1
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
print(f'Prima lista este:{lista1}')
print(f'A doua lista este:{lista2}')
liste_concatenate = lista1+ lista2
print(f'Lista noua, prima metoda: {liste_concatenate}')

#METODA 2
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista1.extend(lista2)
print(f'Lista noua, a doua metoda: {lista1}')

#METODA 3
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista1 +=lista2
print(f'Lista noua, a treia metoda: {lista1}')

#METODA 4
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista_noua = [*lista1, *lista2]
print(f'Lista noua, a patra metoda: {lista_noua}')


#4.
#● Sortează și afișază lista generată la exercițiul anterior.
#● Sortează numărul 0 folosind o funcție.
#● Afișaza iar lista.

lista_noua.sort()
print(f'Lista noua sortata: {lista_noua}')
lista_noua.remove(0)
print(f'Lista noua fara 0: {lista_noua}')


#5. Folosind un if verifică lista generată la exercițiul 3 și afișază:
#● Lista este goală.
#● Lista nu este goală.

#METODA 1
lista_cu_numere = [3, 1, 0, 2, 6, 5, 4]
lista_goala = []
if not lista_goala:
    print('Lista este goala')
else:
    print('Lista contine numere')

#METODA 2
lista_cu_numere = [3, 1, 0, 2, 6, 5, 4]
lista_goala = []
if bool(lista_goala):   #AICI, ATATA TIMP CAT CONDITIA E FALSA (CAZUL MEU) PC-UL VA RETURNA CONDITIA DIN ELSE!!!!!!!!!
    print('Lista este goala')
else:
    print('Lista contine numere')

# METODA 2
lista_cu_numere = [3, 1, 0, 2, 6, 5, 4]
lista_goala = []
if len(lista_goala):
    print('Lista este goala')  #LA FEL CA SI  IN CAZUL CO BOOL
else:
    print('Lista contine numere')


# METODA 3
lista_cu_numere = [3, 1, 0, 2, 6, 5, 4]
lista_goala = []
if len(lista_goala) == 0:
    print('Lista este goala')
else:
    print('Lista contine numere')

#6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista_cu_numere = [3, 1, 0, 2, 6, 5, 4]
lista_cu_numere.clear()
print(lista_cu_numere)

#7. Copy paste la exercițiul 5. Verifică încă o dată.
#Acum ar trebui să se afișeze că lista e goală.

lista_goala = []
if not lista_cu_numere:
    print('Lista este goala') #afiseaza ca lista e goala pentru ca am folosit functia clear
else:
    print('Lista contine numere')

#8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#   Folosește o funcție că să afișezi Elevii (cheile)

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
for key, value in dict1.items():
    print(key)

#9. Printează cei 3 elevi și notele lor
#   Ex: ‘Ana a luat nota {x}’
#   Doar nota o vei lua folosindu-te de cheie

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
for key, value in dict1.items():
    print(f'{key} a luat nota {value}')

#10. Dorel a făcut contestație și a primit 6
#    ● Modifică nota lui Dorel în 6
#    ● Printează nota după modificare

dict1 = {'Dorel': 5}
for key, value in dict1.items():
    if key == 'Dorel':
        dict1[key] = 6
    print(dict1)

#11. Gigel se transferă din clasă
#● Căuta o funcție care să îl șteargă
#● Vine un coleg nou. Adaugă Ionică, cu nota 9
#● Printează noii elevi

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
dict1.pop('Gigel')
dict1.update({'Ionica' :9})
print(dict1)

#12.
#Set
#zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
#weekend = {'sâmbăta', 'duminică'}
#● Adaugă în zilele_sapt ‘luni’
#● Afișeaza zile_sapt

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt.add('luni')
print(zile_sapt)

# 13.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.

zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
if weekend.issubset(zile_sapt):
    print("Subset")
else:
    print('not')

VARIANTA DE PE NET
print("Original list : " + str(zile_sapt))
print("Original sub list : " + str(weekend))
flag = 0
if (all(x in zile_sapt for x in weekend)):
    flag = 1

if (flag):
    print("Yes, list is subset of other.")
else:
    print("No, list is not subset of other.")


#14. Afișează diferențele dintre aceste 2 seturi.
intersectia = zile_sapt.intersection(weekend)
intersectia2 = weekend.intersection(zile_sapt)
print("multimea rezultata din intersectia celor 2 seturi:", intersectia)
print("multimea rezultata din intersectia celor 2 seturi:", intersectia2)

# 15. Afișază intersecția elementelor din aceste 2 seturi.
reuniunea = zile_sapt.union(weekend)
print("multimea rezultata din reuniunea celor 2 seturi este: ", reuniunea)
print(type(reuniunea))


#EXERCITII OPTIONALE
'''
1. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:
● Declară o Listă cu 5 jucători
● Schimbari_efectuate = te joci tu cu valori diferite
● Schimbari_max = 3
Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
- Efectuează schimbarea
- Șterge jucătorul scos din listă
- Adaugă jucătorul intrat
- Afișaza a intra x, a ieșit y, mai ai z schimbări
Dacă jucătorul nu e în teren:
- Afișază ‘ nu se poate efectua schimbarea deoarece jucătorul x nu e în
teren’
- Afișază ‘mai ai z schimbări’
Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”
'''

jucatori = ['J1', 'J2', 'J3', 'J4', 'J5' ]
schimbari_efectuate = 1
schimbari_max = 3
if 'J1' in jucatori:
    jucatori.remove('J1')
    jucatori.append('J6')
    schimbari_max -= 1
    print(f'Lista noua de jucatori este: {jucatori}')
    print(schimbari_max)
#nu inteleg cum  sa fac




















