# 1.Funcție care să calculeze și să returneze suma a două numere

def calcul (a,b):
    suma = a+b
    return suma
print(calcul(5,6))

#2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar

def numar(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(numar(765))

#3. Funcție care returnează numărul total de caractere din numele tău complet.
#(nume, prenume, nume_mijlociu)

def caractere(nume_complet):
    return len(nume_complet)
print(caractere('Cucura Roxana Georgiana')) #adauga si spatiile libere

#4. Funcție care returnează aria dreptunghiului

def aria(lungime, latime):
    return lungime * latime
print(aria(10,9))

#5. Funcție care returnează aria cercului

def arie(raza, pi):
    return (raza ** 2) * pi
print(arie(8, 3.14))

#6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
# și Talse dacă nu găsește.

lista = ('mango', 'cirese', 'cascaval', 'apa')
def cauta(x):
    if x in lista:
        return True
    else:
        return False
print(cauta('mango'))

#7. Funcție fără return, primește un string și printează pe ecran:
#● Nr de caractere lower case este x
#● Nr de caractere upper case exte y
 #-nu stiu


#8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
#numerele pozitive

def lista(list):
    return [element for element in list if element >= 0]
print(lista([-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]))


#9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
#● Primul număr x este mai mare decat al doilea nr y
#● Al doilea nr y este mai mare decat primul nr x
#● Numerele sunt egale.

def numere(x,y):
    if x > y:
        print(f'Primul număr {x} este mai mare decat al doilea număr {y}')
    elif x < y:
        print(f'Al doilea număr {y} este mai mare decat primul număr {x}')
    else:
        print('Numerele sunt egale')
print(numere(78,50))

#10. Funcție care primește un număr și un set de numere.
#● Printeaza ‘am adaugat numărul nou în set’ + returnează True
#● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
#returnează False

def myset(x,y):
    if x in y:
        print("am adaugat numarul nou in set")
        return True
    elif x not in y:
        print('nu am adaugat nr nou in set')
        return False
print(myset(2, {2,3,4,5,6,7,8}))
print(myset(1, {2,3,4,5,6,7,8}))

#EXERCITII OPTIONALE
#1. Funcție care primește o lună din an și returnează câte zile are acea luna

import calendar
import datetime
def an_bisect(year):       #nu am inteles
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(month, year):
    if month in {1,3,5,7,9,31}:
        return 31
    if month == 2:
        if an_bisect(year):
            return 29
        return 28
    return 30

print(days_in_month(2, 2022))  # 31


from calendar import monthrange
def numarul_de_zile_din_luna(year, month):
    return monthrange(year,month)[1] #nu am ineles ce face "[1]"

print(numarul_de_zile_din_luna(2022,7))

#Revizuire tema 5_