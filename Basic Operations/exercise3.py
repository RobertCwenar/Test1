#exercise3.py
#Create 3 variables for each guest: name, age, gender
imie = "Arkadiusz"
wiek = 29 
plec = "Mężczyzna"

imie2 = "Robert"
wiek2 = 28 
plec2 = "Mężczyzna" 

imie3 = "Kasia"
wiek3 = 23
plec3 = "Kobieta"

osoba1 = ('Arkadiusz', 29, 'Mężczyzna')
osoba2 = ('Robert', 28, 'Mężczyzna')
osoba3 = ('Kasia', 23, 'Kobieta')


#crete listaGoscie with 3 guests
listaGoscie = {
            ('Arkadiusz', 29, 'Mężczyzna'), 
            ('Robert', 28, 'Mężczyzna'), 
            ('Kasia', 23, 'Kobieta')}

#crete listaGoscie2 with 3 new guests
listaGoscie2 = {
            ('Wojtek', 15, 'Mężczyzna'), 
            ('Franek', 11, 'Mężczyzna'), 
            ('Basia', 25, 'Kobieta')}

#listaGoscie.append(['Dawid', 40, 'Mężczyzna'])
#listaGoscie.append(['Dominika', 20, 'Kobieta'])

#merge listaGoscie and listaGoscie2 into listaGoscie3
listaGoscie3 = listaGoscie | listaGoscie2


#loop for listaGoscie3 and print each element
for imie, wiek, plec in listaGoscie3:
    print(imie, wiek, plec)