# Exercitiul 1
note_muzicale = ['do','re','mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)
print(note_muzicale[::1])

#Exercitiul 2
note_muzicale = ['do','re','mi', 'fa', 'sol', 'la', 'si', 'do']
x=note_muzicale.count('do')
print(x)

#Exercitiul 3
x=[3,1,0,2]
y=[6,5,4]
x.extend(y)
print(x)

#Exercitiul 4
z=[3,1,0,2,6,5,4]
z.sort()
print(z)
z.remove(0)
print(z)

#Exercitiul 5
z=[3,1,0,2,6,5,4]
if not z:
    print('lista este goala')
else:
    print('lista nu este goala')

#Exercitiul 6
z=[3,1,0,2,6,5,4]
z.clear()
print('z')

#Exercitiul 7
if not z:
    print('lista este goala')
else:
    print('lista nu este goala')

#Exercitiul 8
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

#Exercitiul 9
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print('Ana aluat nota ' + str(dict1['Ana']))
print('Gigel aluat nota ' + str(dict1['Gigel']))
print('Dorel aluat nota ' + str(dict1['Dorel']))

#Exercitiul 10
dict2 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1['Dorel'] = 6
print(dict1)

#Exercitiul 11
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1.pop('Gigel')
print(dict1)
dict2 = { 'Ionica' : 9}
dict1.update(dict2)
print(dict1)

#Exercitiul 12
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

#Exercitiul 13
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
if weekend.issubset(zile_sapt):
    print('Weekend e subset.')
else:
    print('Weekend nu e subset.')

#Exercitiul 14
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
diferente = zile_sapt.difference(weekend)
print(diferente)

#Exercitiul 15
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
intersectia = zile_sapt.intersection(weekend)
print(intersectie)
