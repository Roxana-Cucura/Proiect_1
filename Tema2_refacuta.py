#ex1: is else-evalueaza daca o expresie este adevarata sau falsa, daca conditia esre adevarata atunci o sa se execute "if", altfel se va executa "else" daca condtitia este falsa
#ex2: verifica si afiseaza daca x este nr natural
x = int(input('introdu un numar: '))
if x>0:
    print(f'{x} este numar natural')
else:
    print(f' {x} Nu este numar natural')

#ex 3: verifica daca x este numar pozitiv , negativ sau neutru
x=int(input('Introdu un numar: '))
if x>0:
    print(f'{x} este numar pozitiv')
elif x<0:
    print(f'{x} este negativ')
else:
    print("neutru")

#ex4: verifica si afiseaza daca x este intre -2 si 13
x = int(input("Introdu un numar: "))
if x>14:
    print(f'{x} nu se afla in intreval')
elif x<-3:
    print(f'{x} nu se afla in interval')
else:
   print(f'{x} se afla in interval ')

#ex5: verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x = int(input('Introdu un numar: '))
y = int(input('Introdu un numar: '))
if (x-y)<5:
    print(f'Diferenta este mai mica')
else:
    print('Diferenta mai mare')

#ex 6: verifica daca x NU este intre 5 si 27
x = -43
if not 5 < x < 27:
    print(f' nu e in interval')

x = int(input("Introdu un numar: "))
if x > 28:
    print(f'{x} nu este in interval')
elif x<6:
    print(f'{x} nu este in interval')
else:
    print(f"{x} se afla in intreval")

#ex 7: x,y int, verific si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
x = int(input('Introdu un numar: '))
y = int(input('Introdu al doilea numar: '))
if x==y:
    print("Numerele sunt egale")
elif x > y:
    print(f'{x} este mai mare')
else:
    print(f'{y} este mai mare')

#ex 8: X, y, z - laturile unui triunghi. Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
x = int(input('Introdul prima latura: '))
y = int(input('Introdu a doua latura: '))
z = int(input('Introdu a treia latuta: '))
if (x==y and x!=z) or (z==x and z!=y) or (z==y and y!=x ):
    print("Triunghi isoscel")
elif x == z == y:
    print("Triunghi echilateral")
else:
    print("Triunghi oarecare")

#ex 9: citeste o litera de la tastaura. Verifica si afiseaza daca este vocala sau consoana
litera = input("Introdu o litera: ")
lista_litere = ['a', 'e', 'i','o', 'u']
if litera in lista_litere:
    print('Vocala')
else:
    print("consoana")

#ex 10: transformă și printează notele din sistem românesc în >
'''Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub =>'''

nota = int(input("Introdu nota: "))
if nota >9:
    print('Nota A')
elif nota>8:
    print('Nota B')
elif nota >7:
    print('Nota C')
elif nota >6:
    print('Nota D')
elif nota> 4:
    print("Nota E")
else:
    print("Nota F")

#exercitii optionale: 1.Verifică dacă x are minim 4 cifre (x e int). (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = input("introduceti un numar: ")
print(len(x))
if len(x)==4:
    print(f"x e int")
elif len(x)<4:
    print('x nu e int')
else:
    print('x nu e int')

x = input("introduceti un numar: ")
print(len(x))
if len(x) >=4:
    print(f"x e int")
else:
    print('x nu e int')

#exercitii optionale: 2.Verifică dacă x are exact 6 cifre.
x = input('Introdu numar: ')
print(len(x))
if len(x) == 6:
    print('Are exact 6 cifre')
else:
    print('Nu are 6 cifre')

#exercitii optionale: 3.Verifică dacă x este număr par sau impar (x e int).
x = int(input("Introdu numar: "))
if (x % 2)==0:
    print('par')
else:
    print('impar')

#exercitii optionale: 4. x, y, z (int).Afișează care este cel mai mare dintre ele?
x = int(input('Introdu numar: '))
y = int(input('Introdu al doilea numar: '))
z = int(input('Introdu al treilea numar: '))
if x>y>z:
    print('X mai mare')
elif y>x>z:
    print('Y mai mare')
else:
    print('Z mai mare')


if x > y:
    print('X este mai mare')
elif x > z:
    print('X este mai mare')
elif y > x:
    print('Y mai mare')
elif y > z:
    print('Y mai mare')
elif z > x:
    print('Z mai mare')
elif z > y:
    print('Z mai mare')
else:
    print('Numere egale')

#exercitii optionale: 5. X, y, z - reprezintă unghiurile unui triunghi. Verifică și afișează dacă triunghiul este valid sau nu.
x = int(input('Introdu primul unghi: '))
y = int(input('Introdu al doilea unghi: '))
z = int(input('Introdu al treilea nume: '))

if x + y + z==180 and x>0 and y>0 and z>0:
    print('este triunghi')
else:
    print('nu este triunghi')


#ex bonus:
varsta = int(input('Varsta: '))
insotit_de_mama = input('Este insotit de mama: ')
insotit_de_tata = input('Este insotit de tata: ')
pasaport = input('Are pasaport:' )
act_permisiune_mama = input('Are permisiune mama: ')
act_permisiune_tata = input('Are permisiune tata: ')
if varsta >18 and pasaport == 'da':
     print('Se poate imbarca')
elif varsta < 18 and pasaport == 'da' and insotit_de_mama =='da' and insotit_de_tata =='da' and act_permisiune_mama == 'da' and act_permisiune_tata == 'da':
     print('se poate imbarca')
elif varsta < 18 and pasaport == 'nu' and insotit_de_mama =='da' and insotit_de_tata =='da' and act_permisiune_mama == 'da' and act_permisiune_tata == 'da':
     print(' nu se poate imbarca')
elif varsta < 18 and pasaport == 'da' and insotit_de_mama =='nu' and insotit_de_tata =='da' and act_permisiune_mama == 'da' and act_permisiune_tata == 'da':
     print(' nu se poate imbarca')
elif varsta < 18 and pasaport == 'da' and insotit_de_mama =='da' and insotit_de_tata =='nu' and act_permisiune_mama == 'da' and act_permisiune_tata == 'da':
     print(' nu se poate imbarca')
elif varsta < 18 and pasaport == 'da' and insotit_de_mama =='da' and insotit_de_tata =='da' and act_permisiune_mama == 'nu' and act_permisiune_tata == 'da':
     print(' nu se poate imbarca')
elif varsta < 18 and pasaport == 'da' and insotit_de_mama =='da' and insotit_de_tata =='da' and act_permisiune_mama == 'da' and act_permisiune_tata == 'nu':
     print(' nu se poate imbarca')
else:
    print('Se poate imbarca')

#ex optional-joc cu zarul

import random
num_list = [ 1, 2, 3, 4, 5, 6 ]
random.shuffle(num_list)
print(f'Numarul generat este: {num_list}')

import random
x = random.randint(0, 6)
y = int(input('Tasteaza un numar:'))
if x > y:
    print(f'Mai incearca! Ai ales numarul:{y} si numarul generat a fost:{x}')
elif x < y:
    print(f'Felicitari! Ai castigat! Ai ales numarul:{y} si numarul generat a fost:{x}')
else:
    print(f'Nu te bucura! E egalitate! Ai ales numarul:{y} si numarul generat a fost:{x}')


