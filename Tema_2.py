#Exercitiul 1:
#if else- folosim aceasta combinatie pentru a determina conditia unei instructiuni si pentru a decide ce comenzi sa executam

#Exercitiul 2:
num=int(input('Introdu numar: '))
if num >1:
    print(f'Numarul introdus este natural')
else:
    print(f'Numarul introdus NU este natural')

#Exercitiul 3:
numar=int(input('Introdu numarul:'))
if numar < 1:
    print(f'Numarul este negativ.')
elif numar == 0:
    print(f'Numarul este neutru')
else:
    print(f'Numarul nu corespunde cerintelor')

#Exercitiul 4:
numarul = int(input('Introdu numar: '))
if numarul < 13:
    print(f'Numarul introdus se afla in interval')
elif numarul > -2:
    print(f'Numarul introdus se alfa in interval')
else:
    print('Numarul nu se afla in interval')

#Exercitiul 5:
x = int(input('Scrie primul numar: '))
y = int(input('Scrie al doilea numar: '))
if x - y < 5:
    print('Diferenta dintre x si y este < 5')
else:
    print('Diferenta dintre x si y este > 5')

#Exercitiul 6:
nr = int(input('Introdu numarul: '))
if not x >= 5:
    print('Nu se afla in intervalul [5; -27]')
elif not x <= 27:
    print('Nu se afla in intervalul [5; -27]')
else:
    print('Se afla in intervalul [5; -27]')

#Exercitiul 7:
x = int(input('Introdu un numar: '))
y = int(input('Introdu alt numar: '))
if x == y:
    print('Numere sunt  egale')
elif x > y:
    print('x > y')
else:
    print('x < y')

#Exercitiul 8:
x = int(input('Introdu dimensiunea laturei a: '))
y = int(input('Introdu dimensiunea laturei b: '))
z = int(input('Introdu dimensiunea laturei c: '))
if x == y == z:
    print('Triunghiul este echilateral')
elif x == y or x == z or z == y:
    print('Triunghi este isoscel')
else:
    print('Triunghi este oricare')

#Exercitiul 9:
x = input('Introdu litera: ')
list = ['a', 'e', 'i', 'o', 'u']
if x in list:
    print('Litera este vocala')
else:
    print('litera este consoana')

#Exercitiul 10:
x = int(input('Introdu nota: '))
if x > 9:
    print('A')
elif x > 8:
    print('B')
elif x > 7:
    print('C')
elif x > 6:
    print('D')
elif x > 4:
    print('E')
else:
    print('F')

#Exercitiul 11:

numar = input('Introdu un numar:')
if len(numar) >= 4:
    print('Numarul introdus are 4 cifre')
else:
    print('Numarul introdus nu are 4 cifre')

#Exercitiul 12:
numar = input('Introdu un numar:')
if len(numar) == 6:
    print('Numarul are 6 cifre')
else:
    print('Numarul nu are 6 cifre')

#Exercitiul 13:
nr = int(input('Introdu un numar:'))
if (nr % 2) == 0:
    print('Numarul este par')
else:
    print('Numarul este impar')

#Exercitiul 14:
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))

if x>y>z:
    print('x mai mare ca z')
elif y>x>z:
    print('y mai mare ca z')
else:
    print('z mai mare ')

#Exercitiul 15:
x = int(input('Introdu primului unghi: '))
y = int(input('Introdu al doile unghiului: '))
z = int(input('Introdu al treilea unghiului: '))
if x > 0 and y > 0 and z > 0 and x + y + z <= 180:
    print('Triunghi este valid')
else:
    print('Triunghi nu este invalid')




