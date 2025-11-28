# Napisz program który:
# 1. Dodaje nowe definicje
# 2. Szuka istniejących definicji
# 3. Usuwa wybrane przez użytkownika definicje
# 4. Wyświetla wszystkie definicje w słowniku


definition = {}
print("Welcome in dictionary!")


while True:
    
   
    #print("Dodaj nową definicję: ")
    #print("Szukaj definicji: ")
    #print("Usuń definicję: ")
    #print("Wyświetl wszystkie definicje: ")

    choose = input("Wybierz opcję (dodaj/szukaj/usuń/wyswietl/wyjdz): ")


    
    if choose == "add":
        word = input("Write word: ")
        mean = input("Write definition: ")
        definition [word] = mean 
        print(f"Add new definition '{word}'.")
        
    elif choose == "look for":
        word = input("Write word to looking for: ")
        if word in definition:
            print(f"Definition for '{word}': {definition[word]}")
        else:
            print(f"Słowo '{word}' nie ma w słowniku.")
        
    elif choose == "delete":
        word = input("Podaj słowo, które ma być usunięte:")
        if word in definition:
            print(f'Usunięto definicję dla słowa {word}.')
            del definition[word]
        else:
            print(f"Słowo [word] nie ma w słowniku. ")
        
    elif choose == "wyswietl":
        if definition:
            print("Wyświetl definicje w słowniku:")
            for word, mean in definition.items():
                print(f"{word}: {mean}")
        else:
            print("Słownik nie zawiera żadnych definicji.")
        
    elif choose == "wyjdz":
        print("Wychodzę z programu")
        break
    
    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")

print("Koniec")
    


