# Napisz program który:
# 1. Dodaje nowe definicje
# 2. Szuka istniejących definicji
# 3. Usuwa wybrane przez użytkownika definicje
# 4. Wyświetla wszystkie definicje w słowniku


definition = {}
print("Witaj w słowniku!")
print("Dodaj nową definicję: ")
print("Szukaj definicji: ")
print("Usuń definicję: ")
print("Wyświetl wszystkie definicje: ")

choose = input("Wybierz opcję (dodaj/szukaj/usun/wyswietl/wyjdz): ")

while choose != "wyjdz":
    if choose == "dodaj":
        word = input("Podaj słowo: ")
        mean = input("Podaj definicję: ")
        definition [word] = mean 
        print(f"Dodano definicję dla słowa '{word}'.")

    elif choose == "szukaj":
        word = input("Podaj słowo do wyszukiwania: ")
        if word in definition:
            print(f"Definicja dla '{word}': {definition[word]}")
        else:
            print(f'Słowo {word} nie ma w słowniku.')

    elif choose == "usuń":
        word = input("Podaj słowo, które ma być usunięte:")
        if word in definition:
            print(f'Usunięto definicję dla słowa {word}.')
            del definition[word]