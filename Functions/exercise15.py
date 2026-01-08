import copy 

# copy - płytka 
# deepcopy - głęboka kopia
'''
def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))

    print(toBeDestroyedList)

myList = [1,4, 2,1, 52,3]

print(id(myList))
evil_function((myList[0:5]))

a = 4 
b = 4

# exercise 15.1
a = [1, 2, 3]

b = a 
b.append(4)

print(a)
print(b)    

# exercise 15.2
# Jak używać metody copy() do tworzenia płytkiej kopii listy.
a = [1, 2, 3]
b = a.copy()
b.append(4)

print(a)
print(b)

# exercise 15.3
# Jaka jest różnica między płytką a głęboką kopią zagnieżdżonej listy?

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(100)
print(a)

# exercise 15.4
# Użj funkcji any() aby określić czy lista ma liczby parzyste

numbers1 = [1, 3, 5, 7, 9]
numbers2 = [1, 2, 3, 4, 5]
numbers3 = [2, 3, 6, 9]

def any_even(lista):
   return any ([nr % 2 == 0 for nr in lista])

def all_even(lista):
   return all ([nr % 2 == 0 for nr in lista])

print(any_even(numbers1))
print(any_even(numbers2))
print(any_even(numbers3))

if (any_even(numbers1)):
    print("Lista numbers1 ma liczby parzyste")
else:
    print("Lista numbers1 nie ma liczb parzystych")

if (any_even(numbers2)):
    print("Lista numbers2 ma liczby parzyste")
else:
    print("Lista numbers2 nie ma liczb parzystych")

if (any_even(numbers3)):
    print("Lista numbers3 ma liczby parzyste")
else:
    print("Lista numbers3 nie ma liczb parzystych")

# any - jakikolwiek - funkcja any SPRAWDZA czy jakikolwiek element w iterowalnym jest prawdziwy


# exercise 15.5
# Użyj funkcji all() do określenia, czy osoba posiada wymagany zestaw umiejętności.

def has_required_skills(person, skills):
    return all (skill in person['skills'] for skill in skills)

# Dictionaries representing people with their skills

John = {'name': 'John Doe', 'age': 30, 'skills': ['Python', 'JavaScript', 'C++']}

Filip = {'name': 'Filip Page', 'age': 25, 'skills': ['Java', 'C#', 'Python']}

Michał = {'name': 'Michał Kowalski', 'age': 28, 'skills': ['Python', 'JavaScript', 'Java', 'C#']}

# Required skills
Required_skills = ['Python', 'JavaScript']


# Output results
print(has_required_skills(John, Required_skills))

print(has_required_skills(Filip, Required_skills))  

print(has_required_skills(Michał, Required_skills)) 
'''

# exercise 15.6
# Use ENUMERATE to print a numbered list of tasks.

tasks = ['turning on the washing machine', 'cleaning my room', 'making dinner', 'doing the shopping']


for index, task in enumerate(tasks, start=1):
    print(f"Task {index}: {task.capitalize()}")