# Wyrażenie listowe (list comprehension)
"""
liczby = [3, 5, 2, 8, 6, 1, 4, 7]

potegawanie = []
for liczba in liczby:
    potegawanie.append(liczba ** 2)


liczbyParzyste = []
for liczba in liczby:
    if liczba % 2 == 0:
        liczbyParzyste.append(liczba)


potegiDwojki = [element**2 for element in liczby]

liczbyParzyste2 = [element for # elemety wybierane z listy liczby
                   element in liczby # przechodzimy po elementach listy liczby
                   if element % 2 == 0] # warunek, który musi być spełniony, aby element znalazł się na liście

print(type(liczbyParzyste2))
"""
'''
# Wyrazenie generujące (generator expression)

import sys

evenNumbers = (element
               for element in range(500)
               if element % 2 == 0)

print(type(evenNumbers))

evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0))

print(sum(evenNumbersGenerator))
      
for item in evenNumbersGenerator:
    print(item)

print(sys.getsizeof(evenNumbersGenerator))  # rozmiar generatora w bajtach



# sumowanie wszystkich liczb od 0 do 100 podniesionych do kwadratu

sum = sum 



def my_gen():
   for i in range(11):
       yield i
    
for i in my_gen():
    print(i)


print(type(my_gen()))
'''

# zadanie 7.1
# Napisz generator, który:
# 1. Bierze liczby od 1 do 50.
# 2. Zwraca tylko liczby podzielne przez 3 i niepodzielne przez 2 (czyli np. 3, 9, 15…).
# 3. Policz sumę tych liczb bez tworzenia listy.
# 4. Wypisz te liczby w pętli for.
'''
def numbers_gen():
    for values in range (51):
        if values % 3 ==0 and values % 2 != 0:
            yield values 

sum = sum(numbers_gen())

print(f"Wynik: {sum}")
'''

# wyrażenia słownikowe (dictionary comprehension)
'''
names = {"Robert", "Olek", "Franek", "Zbyszek", "Krzysztof", "Ola"}

numbers = [1, 5, 7, 9, 11, 16]

celcius = {'t1': -15, 't2': -2, 't3': 0, 't4': 15, 't5': 22, 't6': 35}


namelength = {aaaa
            for aaaa in names
              if aaaa.startswith("Z")}




multiplication = [number*number
                  for number in numbers]
                

print(multiplication)

# Wyrażenia zbiorowe (set comprehension)

name = {'arkadiusz', 'bartek', 'Karol', 'Zbyszek', 'jakub', 'marta', 'arek'}
# cwiczenie - usun imiona zaczanające się od litery b i nie kapitalizujące się na A
names = {name.capitalize()
         for name in name
         if not name.startswith('b')
         if not name.lower().startswith('a')}


names1 = {name if name.lower().startswith('a') else name.capitalize()
        for name in name}

for przejdzprzezwszystko in names1:
    #print(przejdzprzezwszystko)

name = {'arkadiusz', 'bartek', 'Karol', 'Zbyszek', 'jakub', 'marta', 'arek'}

# Tworzymy set (zbiór) z listy
names2 = {name1 
          for name1 in name}

# Dodajemy nowe elementy
names2.add("Krzysztof")
names2.add("Kasia")

print(names2)

'''