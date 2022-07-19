#ex 12:indexul de start al cuvantului rock
prop = 'Coral is either the stupidest animal or the smartest rock'
x=prop.find('rock')
print(x)
print(prop[:x])
print(len(prop))
print(prop[0:-5])

#ex13
nr = '0123456789'
print(nr[::2]) #pare
print(nr[1::2]) #impare

# Exercitiul 15:
r ='0123456789'
s = r.isnumeric()
print(s)

#exercitiu optional 1: citeste de la tastatura un string de dimensiune impara, afiseaza caracterul din mijloc
ex = 'penar'
print(ex[2:-2])

text = str(input("Scrie: "))
print(f'sirul de caractere este: { (len(text) % 2) == 0}')
print(f"caracterul din mijloc este: {text[(len(text)//2)]}")

#ex optional-ultinul
user = str(input('Introdul user-ul: '))
parola = str(input('Introdu parola: '))
print(f'Parola pentru userul {user} este {parola} si are {len(user) + len(parola)}')