'''
    TEMA NR. 0
EXERCITIUL 2. Ce este o variabila STRING?
              R: Variabila de tip STRING reprezinta un sir de caractere delimitat de ghilimele simple  ' '
EXERCITIUL 4. Declara si initializeaza in limbajul de programare python cate o variabila din fiecare din urmatoarele tipuri: string, integer, float, boolean.
'''

#creare STRING
tip_tensiune = 'de linie'
#afisare STRING
print(f'Tensiune: {tip_tensiune}')

#creare INTEGER
valoare_data = 256
#afisare INTEGER
print(f'Valoare tensiune data:{valoare_data}')

#creare FLOAT
valoare_masurata = 267.67
#afisare FLOAT
print(f'Valoarea masurata a tensiunii:{valoare_masurata}')

#creare BOOLEAN
se_masoara_in_volti = True
#afisare BOOLEAN
print(f'Se masoara in volti:{se_masoara_in_volti}')

'''
EXERCITIUL 6. Scrie segmentul de cod de la exercitiul 5 din JAVA in limbajul de programare Python.
int i;
for (i=1; i<20; i = i+3)
System.out.println( i );
'''

i=1
while i<20:
    print(i, end = " ")
     i= i+3


