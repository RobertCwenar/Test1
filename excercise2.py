#List Variables
lista = [3, 5, 7, 10, 134, 67, 87.9, 56, 890]

#Operations 
add = sum(lista)
avg = round(add/len(lista), 2)
max = max(lista)
min = min(lista)

#Instructions
print(f"Suma liczb: {add}")
print(f"Średnia: {avg} jest średnią z listy." )
print(f"Maksymalna wartość wynosi: {max}, a minimalna wartość: {min}.")
