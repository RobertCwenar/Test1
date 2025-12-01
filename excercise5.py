# Napisz program który:
# 1. Dodaje nowe definicje
# 2. Szuka istniejących definicji
# 3. Usuwa wybrane przez użytkownika definicje
# 4. Wyświetla wszystkie definicje w słowniku


definition = {}
print("Welcome to the dictionary!")


while True:
    
   
    #print("Dodaj nową definicję: ")
    #print("Szukaj definicji: ")
    #print("Usuń definicję: ")
    #print("Wyświetl wszystkie definicje: ")

    choose = input("Choose option (add/look for/delete/display/exit): ")


    
    if choose == "add":
        word = input("Write word: ")
        mean = input("Write definition: ")
        definition[word] = mean 
        print(f"Added new definition '{word}'.")
        
    elif choose == "look for":
        word = input("Write word to look for: ")
        if word in definition:
            print(f"Definition for '{word}': {definition[word]}")
        else:
            print(f"Word '{word}' is not in the dictionary.")
        
    elif choose == "delete":
        word = input("Write word to delete: ")
        if word in definition:
            print(f'Delete definition for word {word}.')
            del definition[word]
        else:
            print(f"Word '{word}' does not in dictionary. ")
        
    elif choose == "display":
        if definition:
            print("Display definition in the dictionary:")
            for word, mean in definition.items():
                print(f"{word}: {mean}")
        else:
            print("The dictionary does not contain any data.")
        
    elif choose == "exit":
        print("Exiting program.")
        break
    
    else:
        print("Wrong option. Try again.")

print("The end.")
    


