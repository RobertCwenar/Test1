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

with open("WorkwithFiles/oceany.txt", "r", encoding="utf-8") as file:
    oceany1 = file.readlines()  # wrzuci wszystko w listę


print(oceany1)

with open("WorkwithFiles/oceany.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # usuwa białe znaki z początku i końca linii   