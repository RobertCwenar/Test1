"""try:
    file = open("test.txt", "w") # UCHWYT HANDLE
    file.write("sample")

    print(0/0)
    a =5
    file.write("sample")
finally:
    file.close()
"""

with open("WorkwithFiles/oceany.txt", "r") as file:
    oceany = file.read().splitlines()


print(oceany)