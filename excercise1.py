#Szukana liczba zadanie
szukana = 7
Zgadywana = 0 

while Zgadywana != szukana:
    Zgadywana = int(input("Podaj Liczbę: "))
if Zgadywana < szukana:
    print("Za mało")
elif Zgadywana > szukana:
    print("Za dużo")

print("Brawo to jest szukana wartość!")