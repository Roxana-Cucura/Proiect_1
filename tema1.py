'''Exercitiul 1:
VARIABILA = zona din memoria unui calculator care tine date'''

# Exercitiul 2:
curent = 'de faza'
valoare_data = 4
valoare_masurata = 4.7
se_masoara_in_amperi = True
print(f'Curent:{curent}')
print(f'Valoarea curentului dat :{valoare_data}')
print(f'Valoarea curentului masurat :{valoare_masurata}')
print(f'Se masoara in A?: {se_masoara_in_amperi}')

# Exercitiul 3:
a = 'de faza'
b = 4
c = 4.7
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Exercitiul 4:
e = 4.7
e = round(e)
print(e)
print(type(e))

# Exercitiul 5:
tip_masina = ' de inductie'
tensiunea_de_linie = 400
factor_de_putere = 0.82
rotor_in_colivie = True
print(f'Se de o masina {tip_masina}, care are tensiunea egala cu: {tensiunea_de_linie} V, factorul de putere egal cu : {factor_de_putere} si are rotor in colivie: {rotor_in_colivie}.')

tip_analize = 'medicale'
calciu = 10
fier = 1.8
valori_normale = True
print(f'Analize {tip_analize}, valoarea pentru calciu este :{calciu} mg/100ml, iar valoarea fierului este :{fier} g/l, acestea reprezinta valori normale:{valori_normale}.')

dieta_caini = 'somon si ovaz'
proteine = 10
calorii = 2803.08
ovazul_nefiert= False
print(f'Dieta pentru caini cu {dieta_caini}, hrana ca atare contine {proteine}% proteine, numarul de calorii este {calorii} per reteta iar ovazul poate fi servit nefiert: {ovazul_nefiert}.')

locatia = 'Berlin'
an = 1944
data = 12.11
atacuri_impotriva_poporului= False
print(f'Generalul Vlasov, odata ajuns la {locatia} , in anul {an} , la data de {data} , anunta o serie de atacuri impotriva poporului:{atacuri_impotriva_poporului}.')

# Exercitiul 6:

f = input('Nume:')
print(f)
g = input('Prenume:')
print(g)
print(f'Numele complet are:{len(f + g)} caractere')

# Exercitiul 7:
h = input('Lungimea este:')
print(h)
i = input('Latimea este:')
print(i)
aria = int(h) * int(i)
print(f'Aria dreptunghiului este:{aria} centimetri')

#Exercitiul 8:
j = 'Coral is either the stupidest animal or the smartest rock'
print(len(j))
k = int(input('Scrie un numar:'))
if k >40:
      print(j)
else:
      print(j[0:57 - k])

# Exercitiul 9:
l = 'Coral is either the stupidest animal or the smartest rock'
print(len(l))
print(l[0:5] + l[-5:58])

# Exercitiul 10:
m = 'Coral is either the stupidest animal or the smartest rock'
print(m.count('the'))

# Exercitiul 11:
n = 'Coral is either the stupidest animal or the smartest rock'
o = n.replace('the', 'THE')
print(o)

# Exercitiul 12:
p = 'Coral is either the stupidest animal or the smartest rock'
print(len(p) - 3)
print(p[:53])

# Exercitiul 14:
q = '0123456789'
print(q[1::2])
print(q[::2])

# Exercitiul 15:
r ='0123456789'
s = r.isnumeric()
print(s)

# Exercitiul 16:
t = (input('Srie un cuvant de dimensiune impara:'))
def middle_char(t):
    return t[(len(t)-1)//2:(len(t)+2)//2]
print('Caracterul din mijloc este ' + middle_char(t))

# Exercitiul 17:
u = input('Cuvantul e palindrom: ')
v = u[::-1]
assert u == v
print('cuvantul e palindrom')

# Exercitiul 20:
user = input('Scrie user-ul: ')
parola = input('Scrie parola: ')
w = len(parola)
print(f'Parola pentru {user} este {parola} si are {w} caractere')