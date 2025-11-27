# Słownik w liście - ćwiczenia

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},
        "4WW4F4HiUTP5dBdHatPw": {'name': 'Marie', 'age': 2, 'sex': 'Female'},
        "yuHhrXS1xsSql7kIEnUH": {'name': 'Leila', 'age': 24, 'sex': 'Female'},
        "76XBNSkJn1BIRoX3hB0s": {'name': 'Eric', 'age': 27, 'sex': 'Male'},
        "dMii4kQO1XW4WoiVI7S4": {'name': 'Tobey', 'age': 22, 'sex': 'Female'},
        "DU3Zi0aNj2LLAfujLUWB": {'name': 'Missy', 'age': 25, 'sex': 'Female'}           
         }

people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
        ]


people3 = ['Robert', 
            'Dawid', 
            'Anna',
            'Kasia']

people4 = {
            "Id1": {'name': 'Robert', 'age': 30, 'sex': 'Male'},
            "Id2": {'name': 'Dawid', 'age': 25, 'sex': 'Male'},
            "Id3": {'name': 'Anna', 'age': 13, 'sex': 'Female'},
            "Id4": {'name': 'Kasia', 'age': 22, 'sex': 'Female'},
            "Id5": {'name': 'Aleksander', 'age': 31, 'sex': 'Male'}, 
            "Id6": {'name': 'Krzysztof', 'age': 31, 'sex': 'Male'},
            "Id7": {'name': 'Jagoda', 'age': 26, 'sex': 'Female'}
            }

people5 = {
            "Id1": {'name': 'Arek', 'car': 'Ford', 'girlfriend': 'Anna'},
            "Id2": {'name': 'Michał', 'car': 'BMW', 'girlfriend': 'Kasia'},
            "Id3": {'name': 'Daniela', 'car': 'Audi', 'boyfriend': 'Tomek'},
            "Id4": {'name': 'Zofia', 'car': 'Mercedes', 'boyfriend': 'Piotrek'},
            "Id5": {'name': 'Kamil', 'car': 'Toyota', 'girlfriend': 'Magda'},
            "Id6": {'name': 'Anna', 'car': 'Honda', 'boyfriend': 'Arek'}, 
            "Id7": {'name': 'Kasia', 'car': 'Fiat', 'boyfriend': 'Michał'}, 
            "Id8": {'name': 'Tomek', 'car': 'Seat', 'girlfriend': 'Daniela'}, 
            "Id9": {'name': 'Piotrek', 'car': 'Opel', 'girlfriend': 'Zofia'}, 
            "Id10": {'name': 'Magda', 'car': 'Hyundai', 'boyfriend': 'Kamil'},
            }

ratings1 = {
        "Arkadiusz": (2,1,2,3,2,3),
        "Wiola": (4,2,1,3,4),
        "Robert": (5,5,4,4,5), 
        "Gosia": (5,6,2,3,1)
    }

ratings2 = [
        {"name": "Arkadiusz", "ratings": (2,1,2,3,2,3), 'behavior': 4},
        {"name": "Agness", "ratings": (4,2,1,3,4), 'behavior': 2}
    ]

ratings3 = {
        "Arkadiusz": {'ratings': (2,1,2,3,2,3), 'behavior': 4},
        "Agness": {'ratings': (4,2,1,3,4), 'behavior': 2}
    }

"""
for key in ratings1:
    print(f"{key} ratings: (ratings[key])")


for value in people3:
    print(f"Person Name: {value}")

for person in people2:
    for key in person:
        print(f"{key}: {person[key]}")
        

for Id in people: 
    for key in people[Id]:
        print(f"{key}: {people[Id][key]}")
  

for value in people4:
    for key in people4[value]:
        print(f"{key}: {people4[value][key]}")


for val in people5:
    for key in people5[val]:
        print(f"{key}: {people5[val][key]}")


for id, dictionary in people5.items():
    print(f"ID: {id}")
    for key in dictionary:
        print(f"  key, dictionary[key]")
"""

