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

listaGoscie = {
            ('Arkadiusz', 29, 'Mężczyzna'), 
            ('Robert', 28, 'Mężczyzna'), 
            ('Kasia', 23, 'Kobieta')}


listaGoscie2 = {
            ('Wojtek', 15, 'Mężczyzna'), 
            ('Franek', 11, 'Mężczyzna'), 
            ('Basia', 25, 'Kobieta')}

#listaGoscie.append(['Dawid', 40, 'Mężczyzna'])
#listaGoscie.append(['Dominika', 20, 'Kobieta'])

listaGoscie3 = listaGoscie | listaGoscie2

for imie, wiek, plec in listaGoscie3:
    print(imie, wiek, plec)