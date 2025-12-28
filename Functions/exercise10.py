# Write a function that takes a list of numbers and returns the sum of all positive numbers.
# The function should ignore negative numbers and zero in the list.

'''
numbers = [-10, 4, -5,3, 0, 7, -41, 100, -3, 90]

def sum_positive_numbers(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num 
    return total
print(f"Sum of the positive numbers is: {sum_positive_numbers(numbers)}" )
'''


definitions = {}

def add_definition(definitions, key, definition):
    definitions[key] = definition
    print("Definicja dodana pomyślnie")

def find_definition(definitions, key):
    if key in definitions:
        print(definitions[key])
    else:
        print("Nie znaleziono definicji o nazwie", key)


def delete_definition(definitions, key):
    if key in definitions:
        del definitions[key]
        print("Usunięto definicję o nazwie:", key)
    else:
        print("Nie znaleziono definicji o nazwie", key)
 
while(True):
    print("1: Dodaj definicję")
    print("2: Znajdź definicję")
    print("3: Usuń definicję")
    print("4: Zakończ")
 
    choice = input("Co chcesz zrobić? ")

    if choice == "1":
        key = input("Podaj klucz (słowo) do zdefiniowania: ")
        definition = input("Podaj definicję: ")
        add_definition(definitions, key, definition)
    elif choice == "2":
        key = input("Czego szukasz? ")
        find_definition(definitions, key)
    elif choice == "3":
        key = input("Jaką definicję chcesz usunąć? ")
        delete_definition(definitions, key)
    elif choice == "4":
        print("Do widzenia!")
        break 
    else:
        print("Podałeś coś z poza zakresu")